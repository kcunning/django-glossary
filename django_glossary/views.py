import string
from django.db.models import Q
from django.views.generic import DetailView, ListView
from django_glossary.models import Term


class TermListView(ListView):
    model = Term
    context_object_name = "terms"
    paginate_by = 20
    ordering = 'title'

    def get_context_data(self, **kwargs):
        context = super(TermListView, self).get_context_data(**kwargs)

        # import ipdb; ipdb.set_trace()

        terms = self.model.objects.all()

        if "q" in self.request.GET:
            query = self.request.GET['q']
            terms = terms.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(synonyms__title__icontains=query)
            ).distinct()
            try:
                starts_with = query[0]
            except IndexError:
                starts_with = ''
        else:
            query = ''
            starts_with = self.request.GET.get("l", "a").lower()
            terms = terms.filter(title__istartswith=starts_with)

        used_letters = list(set(self.model.objects.distinct().extra(
            select={'f_letter': "lower(substr(title,1,1))"}
        ).values_list('f_letter', flat=True)))

        context.update({
            'a_z': string.ascii_lowercase,
            'query': query,
            'starts_with': starts_with,
            'used_letters': used_letters,
        })

        return context


class TermDetailView(DetailView):
    model = Term
    context_object_name = "term"
