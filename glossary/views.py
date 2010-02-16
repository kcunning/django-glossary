import string

from django.db.models import Q

from django.views.generic.list_detail import object_list

from .models import Term

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
            Q(title__contains=query)
            | Q(description__contains=query)
            | Q(synonyms__title__contains=query)
        ).distinct()
    else:
        initial = request.GET.get("l", "a").lower()
        ec['starts_with'] = initial
        terms = terms.filter(title__startswith=ec['starts_with'])

    return object_list(request, queryset=terms, extra_context=ec, **kwargs)