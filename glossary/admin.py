from django.contrib import admin
from glossary.models import Term

class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ['title']}
    list_display = ('title',)
    search_fields = ('title', 'description')

admin.site.register(Term, TermAdmin)