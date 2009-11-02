from django.contrib import admin
from glossary.models import Term

class TermAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ['title']}

admin.site.register(Term, TermAdmin)