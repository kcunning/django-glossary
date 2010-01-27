from django.test.client import Client
from glossary.models import Term, Synonym
from django.test import TestCase
import unittest

class GlossaryTestCase(TestCase):
	#TODO: Fix ABC nav result!
	
	def setUp(self):
		self.ace = Term.objects.create( title="Ace", slug = "ace", description="Description for Ace")
		self.base = Term.objects.create( title="Bace", slug = "base", description="Ace of BASE!")
		self.case = Term.objects.create( title="Case", slug = "case", description="Make a case")
		self.dace = Term.objects.create( title="Dace", slug = "dace", description="A dude named Dace")
		self.eco = Term.objects.create( title="Eco", slug = "eco", description="Eco-awesomeness")
		self.face = Term.objects.create( title="Face", slug = "face", description="In your face!")
		self.gale = Term.objects.create( title="Gale", slug = "gale", description="Dorothy Gale?")
		self.hail = Term.objects.create( title="Hail", slug = "hail", description="Hail of fail")
		self.ill = Term.objects.create( title="Ill", slug = "ill", description="That coat is ill.")		
		self.synonym = Synonym.objects.create(title="Synonym", term = self.ace)
		
	def tearDown(self):
		pass
		
	def test_term(self):		
		self.assertEquals(self.ace.title, self.synonym.term.title)
		self.assertEquals(self.ace.slug, "ace")
		
		
	def test_term_view(self):		
		response = self.client.get('/glossary/')
		self.assertTrue(response.status_code == 200)
		
		response = self.client.get('/glossary/ace/')
		self.assertTrue(response.status_code == 200)
		self.assertContains(response, "Ace")
		self.assertContains(response, "Description for Ace")
		
		response = self.client.get('/glossary/?l=a')
		self.assertTrue(response.status_code == 200)
#		self.assertContains(response, "Ace")						#TODO - Fix me!
		self.assertContains(response, '<li class="current"><a href = "?l=a">a</a></li>')
		
		response = self.client.get('/glossary/?q=dude')
		self.assertTrue(response.status_code == 200)
		self.assertContains(response, "Dace") 
		self.assertContains(response, '<input type="text" name="q" id="id_q" value="dude"')
		
		
