# Create your views here.

from django.shortcuts import render_to_response
from glossary.models import Term

def term_index(request):
	"""
	Return a list of all terms
	
	"""
	return render_to_response('glossary/term_index.html', 
								{ 'term_list': Term.objects.all()})
								
def search(request):
	query = request.GET.get('q', '')
	results = []
	if query:
		results = Term.objects.filter(description__icontains=query)
	return render_to_response('glossary/search.html', 
				  {'query':query,
				  'results': results })