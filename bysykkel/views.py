import sys
import re
import xml.etree.ElementTree as ET
import xml.sax.saxutils as sax
from urllib import urlopen
from django.views.generic.simple import direct_to_template
from bysykkel.models import Rack

def index(request):
	return direct_to_template(request, 'rack/index.html', {'racks': Rack.objects.all()})

def detail(request, rack_id):
	rack = parse_rack(rack_id)
	return direct_to_template(request, 'rack/rack.html', {'rack': rack})
	
# update racks stored in database, used for google maps
def update_static_racks(request):
	RACKS_URL = 'http://smartbikeportal.clearchannel.no/public/mobapp/maq.asmx/getRacks'
	NAMESPACE = '{http://smartbikeportal.clearchannel.no/public/mobapp/}'
	
	 # get all rack station ids
	racks_xml = urlopen(RACKS_URL).read()
	racks_tree = ET.fromstring(sax.unescape(racks_xml))
	racks = racks_tree.findall('{0}station'.format(NAMESPACE))
	
	# delete all stations previously loaded
	# Racks.objects.all().delete()
	Rack.objects.all().delete()
	for rack_station in racks:
		# 500 and over are for testing?
		if int(rack_station.text) < 2:
		
			rack = parse_rack(int(rack_station.text))
			
			Rack(id = int(rack_station.text), description = rack["description"], lat = rack["lat"], lng = rack["lng"]).save()
	return direct_to_template(request, 'static_racks/index.html', {'racks': Rack.objects.all()})

def parse_rack(id):
	RACK_URL = 'http://smartbikeportal.clearchannel.no/public/mobapp/maq.asmx/getRack?id={0}'
	NAMESPACE = '{http://smartbikeportal.clearchannel.no/public/mobapp/}'
	XMLQUERY = '{0}station/{0}{1}'
	
	rack_xml = urlopen(RACK_URL.format(id)).read()
	tree = ET.fromstring(sax.unescape(rack_xml))
	
	# if rack is offline, return
	if tree.find(XMLQUERY.format(NAMESPACE, 'online')).text == '':
		return
	rack = {}
	rack["id"] = id
	rack["description"] = re.split('[0-9]+-', tree.find("{0}station/{0}description".format(NAMESPACE)).text)[1]
	rack["ready_bikes"] = int(tree.find("{0}station/{0}ready_bikes".format(NAMESPACE)).text)
	rack["empty_locks"] = int(tree.find("{0}station/{0}empty_locks".format(NAMESPACE)).text)
	rack["online"] = tree.find("{0}station/{0}online".format(NAMESPACE)).text
	rack["lat"] = float(tree.find("{0}station/{0}latitude".format(NAMESPACE)).text)
	rack["lng"] = float(tree.find("{0}station/{0}longitute".format(NAMESPACE)).text)
	return rack


def parsefile(path):
   try:
      file = open(path, "r")
      fileread = file.read()
      fileread = sax.unescape(fileread.decode('utf-8')).encode('utf-8')
      file.close()
   except:
      print "Reading File Bug"
      sys.exit(1)
   return ET.fromstring(fileread)