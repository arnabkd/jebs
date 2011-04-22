from urllib import urlopen
import xml.etree.ElementTree as ET
import xml.sax.saxutils as sax
from django.shortcuts import render_to_response
from static_racks.models import Racks, Rack
import re
# Create your views here.


def get_racks(request):
	RACKS_URL = 'http://smartbikeportal.clearchannel.no/public/mobapp/maq.asmx/getRacks'
	RACK_URL = 'http://smartbikeportal.clearchannel.no/public/mobapp/maq.asmx/getRack?id={0}'
	NAMESPACE = "{http://smartbikeportal.clearchannel.no/public/mobapp/}"
    
    # get all rack station ids
	racks_xml = urlopen(RACKS_URL).read()
	racks_tree = ET.fromstring(sax.unescape(racks_xml))
	racks = racks_tree.findall('{0}station'.format(NAMESPACE))
	
	# delete all stations previously loaded
	# Racks.objects.all().delete()
	Rack.objects.all().delete()
	
	for rack_station in racks:
		# 500 and over are for testing?
		if int(rack_station.text) < 5:
			# Racks(rack_id = rack_station.text).save()
			
			# get url
			rack_xml = urlopen(RACK_URL.format(rack_station.text)).read()
			rack_tree = ET.fromstring(sax.unescape(rack_xml))
			# remove id in the beginning of description
			desc = re.split('[0-9]+-', rack_tree.find("{0}station/{0}description".format(NAMESPACE)).text)[1]
			Rack(rack_id = int(rack_station.text), description = desc, lat = float(rack_tree.find("{0}station/{0}latitude".format(NAMESPACE)).text), lng = float(rack_tree.find("{0}station/{0}longitute".format(NAMESPACE)).text)).save()
			
			
	return render_to_response('static_racks/index.html', {'Racks': Racks.objects.all()})