from django.db import models

class Racks(models.Model):
	rack_id = models.IntegerField()
	
	def __unicode__(self):
		return 'Stasjonsnummer: ' + str(self.rack_id)

class Rack(models.Model):
	rack_id = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=200)
	lat = models.FloatField()
	lng = models.FloatField()
	
	def __unicode__(self):
		return self.description