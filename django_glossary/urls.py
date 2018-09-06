from django.conf.urls import url
from .views import TermDetailView, TermListView


app_name = 'django_glossary'
urlpatterns = [
    url(r'^$', TermListView.as_view(), name='glossary-list'),
    url(r'^(?P<slug>[-\w]+)/$', TermDetailView.as_view(), name='detail'),
]
