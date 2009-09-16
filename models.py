from django.db import models

# Create your models here.
# Okay!

class Term(models.Model):
	title = models.CharField(max_length=250)
	slug = models.SlugField(unique=True)
	description = models.TextField()
	acronym = models.CharField(max_length=250, blank=True)
	long_name = models.CharField(max_length=250, blank=True)
	
	class Meta:
		ordering = ['title']
		
	def get_absolute_url(self):
		return '/glossary/%s/' % self.slug
	
	
	def __unicode__(self):
		return self.title
	