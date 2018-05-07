from django.contrib import admin
from django_glossary.models import Term, Synonym


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ('title',)
    search_fields = ('title', 'description')


@admin.register(Synonym)
class SynonymAdmin(admin.ModelAdmin):
    pass