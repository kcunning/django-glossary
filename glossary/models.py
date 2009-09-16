from django.db import models

# Create your models here.
# Okay!

class Term(models.Model):
	"""
	A single glossary term
	
	# Create a term
	>>> test = Term.objects.create(	title="Test", slug = "test", description="A thing I stick in a doc string", acronym="DST",long_name="Doc String Test")
	
	# Call the generic classes
	>>> test.get_absolute_url()
	'/glossary/test/'
	>>> test.__unicode__()
	'Test'
	
	# Now lets test some pages
	>>> from django.test.client import Client
	>>> c = Client()
	>>> response = c.get('/glossary/test/')
	>>> response.status_code
	200
	>>> response.content
	'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 ...'
	>>> response = c.get('/glossary/')
	>>> response.status_code
	200
	>>> response.content
	'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 ...'
	"""
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
	