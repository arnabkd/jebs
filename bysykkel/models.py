from django.db import models

class Rack(models.Model):
	id = models.IntegerField(primary_key=True)
	description = models.CharField(max_length=200)
	lat = models.FloatField()
	lng = models.FloatField()
	
	def __unicode__(self):
		return self.description