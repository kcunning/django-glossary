from django import template
register = template.Library()

from django.shortcuts import render_to_response
from glossary.models import Term

@register.inclusion_tag('glossary/glossary_list.html')
def glossary_list(page):
	glossary_items = []
	
	content = page.content
	
	while content.__contains__('[['):
		start = content.find('[[')+2
		end = content.find(']]')
		term = content[start:end]
		content = content[end+2:content.__len__()]
		glossary_items.append(term)
	terms = []
	for term in glossary_items:
		t = Term.objects.filter(title=term)
		if t:
			terms.append(t[0])
	print terms
	return {"terms": terms,}

