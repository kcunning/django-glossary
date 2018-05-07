from django.conf.urls import url
from .views import TermDetailView, TermListView
from django_glossary.models import Term



# terms = Term.objects.all()
#
#
# urlpatterns = patterns('',
#     url(r'^$',                     'glossary.views.term_list', {"paginate_by": 20}, name="glossary-list"),
#     url(r'^(?P<slug>[-\w]+)/$',    'django.views.generic.list_detail.object_detail', {"queryset": terms}, name="glossary-detail"),
# )


########

urlpatterns = [
    url(r'^$', TermListView.as_view(), name='glossary-list'),
    url(r'^(?P<slug>[-\w]+)/$', TermDetailView.as_view(), name='detail'),
]