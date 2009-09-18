from django.conf.urls.defaults import *

# These are sample URL patterns for you! Chances are, you'll want to splice this app up how you need.

urlpatterns = patterns('',
	(r'^$', 'glossary.views.term_index'),
	(r'^search/$', 'glossary.views.search'),
	(r'^abc_nav/', 'glossary.views.abc_nav'),

)