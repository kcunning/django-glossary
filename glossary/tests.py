from django.test.client import Client
from glossary.models import Term, Synonym
from django.test import TestCase

class GlossaryTestCase(TestCase):
	fixtures = ["core_pages.json","glossary.json"]
	
	def setUp(self):
		pass
		
	def tearDown(self):
		pass
		
	def test_term(self):
		self.assertTrue(Term.objects.count(), 1)
		self.assertTrue(Synonym.objects.count(), 1)
		
	def test_term_view(self):
		response = self.client.get('/glossary/')
		self.assertTrue(response.status_code == 200)
		
		response = self.client.get('/glossary/aas/')
		self.assertTrue(response.status_code == 200)
		
		term = Term.objects.get(slug = "aas")
		syn = Synonym.objects.get(term = term)
		self.assertContains(response, syn.title)
		
