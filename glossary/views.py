import string

from django.db.models import Q

from django.views.generic.list_detail import object_list
from django.db import connection, transaction

from glossary.models import Term

def term_list(request, **kwargs):
    """
    Return a list of all terms

    """

    ec = {"a_z": string.lowercase}

    terms = Term.objects.all()

    if "q" in request.GET:
        query = request.GET['q']
        ec['query'] = query
        terms = terms.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
            | Q(synonyms__title__icontains=query)
        ).distinct()
    else:
        initial = request.GET.get("l", "a").lower()
        ec['starts_with'] = initial
        terms = terms.filter(title__istartswith=ec['starts_with'])

    terms = terms.extra(select={"lower_title": "LOWER(%s.title)" % Term._meta.db_table }).order_by("lower_title")
    
    used_letters = []
    for i in ec["a_z"]:
        try:
            x = Term.objects.get(title__startswith=i)
            used_letters.append(i)
        except:
            pass
    

    return object_list(request, 
                        queryset=terms, 
                        extra_context={'ec': ec,
                                        'starts_with': ec['starts_with'],
                                        'a_z': ec['a_z'],
                                        'used_letters': used_letters},
                        **kwargs)
