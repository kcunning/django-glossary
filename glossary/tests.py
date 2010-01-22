from django.test.client import Client
from glossary.models import Term, Synonym
from django.test import TestCase
import unittest

class GlossaryTestCase(TestCase):
#	fixtures = ["core_pages.json","glossary.json"]
	
	def setUp(self):
		self.term = Term.objects.create( title="Test", slug = "test", description="A thing I stick in a unit test")
		self.synonym = Synonym.objects.create(title="Synonym", term = self.term)
		
	def tearDown(self):
		pass
		
	def test_term(self):
		self.assertTrue(Term.objects.count(), 1)
		self.assertTrue(Synonym.objects.count(), 1)
		
	def test_term_view(self):
		
		self.assertEquals(self.term.title, self.synonym.term.title)
		self.assertEquals(self.term.slug, "test")
		
		term = Term.objects.get(slug = "test")
		syn = Synonym.objects.get(term = term)
		
