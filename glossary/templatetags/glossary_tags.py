from django import template
register = template.Library()

from glossary import models

@register.inclusion_tag('glossary/glossary_list.html')
def glossary_list(page):
	glossary_items = []
	
	content = page.content
	
	while content.__contains__('[['):
		print content
		start = content.find('[[')+2
		end = content.find(']]')
	
		term = content[start:end]

		content = content.lstrip(content[0:end+2])

		glossary_items.append(term)
	
	print glossary_items
	return {
		"glossary_items": glossary_items,
	}

