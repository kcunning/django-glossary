#Django Glossary

Purpose
-------
Create a glossary for a Django website.

Current features
----------------
A user can add terms. \o/
Terms are displayed on a single page with term, synonyms, and definition.
Search!
ABC quick nav

Roadmap for the future:

 - Multiple glossaries per site
 - Pop-up rendering on rich text fields

Install:

 - settings.py: add `django_glossary` to `INSTALLED_APPS`
 - urls.py: add ` url(r'^glossary/', include('django_glossary.urls')),` to `urlpatterns`
 - override templates in: templates/django_glossary

Compatibility
----------------
Last tested with: Django 1.11.15