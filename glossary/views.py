# Create your views here.

from django.shortcuts import render_to_response
from glossary.models import Term

def term_index(request):
	return render_to_response('glossary/term_index.html', 
								{ 'term_list': Term.objects.all()})