# Create your views here.

import string

from django.shortcuts import render_to_response
from django.conf import settings
from glossary.models import Term

def term_index(request):
	"""
	Return a list of all terms
	
	"""
	return render_to_response('glossary/term_index.html', 
								{ 'term_list': Term.objects.all(),
								'MEDIA_URL': settings.MEDIA_URL, })
								
def term(request):
	return render_to_response('glossary/term.html',
							{ 'term':'Pluto'})
								
def search(request):
	from django.db import connection, transaction
	cursor = connection.cursor()
	
	query = request.GET.get('q', '')
	results = []

	query2 = "%%" + query + "%%"
	subquery = 'select distinct title from glossary_term where (title LIKE "%s") or (description LIKE "%s") or (acronym LIKE "%s") or (long_name LIKE "%s")' % (query2, query2, query2, query2)
	
	cursor.execute(subquery)
	results = cursor.fetchall()
	
	if query:
		cursor.execute(subquery)
		results = cursor.fetchall()
		r = []
		for result in results:
			r.append(result[0])
		results = r
		results2 = Term.objects.filter(title__in=results)
	else:
		results2 = []
	return render_to_response('glossary/search.html', 
				  {'query':query,
				  'results': results2 })

		
def abc_nav(request):	
	url = request.get_full_path()
	letter = url[url.__len__()-1]
	results = []
	
# 	if url[url.__len__()-5:url.__len__()-1] == "/?q=":
	results = Term.objects.filter(title__istartswith=letter)

	a-z = list(string.ascii_uppercase)
	
	return render_to_response('glossary/abc_nav.html',
					{'a_z':a_z,
					'url':url,
					'letter':letter,
					'results':results,
					'MEDIA_URL': settings.MEDIA_URL,})
	