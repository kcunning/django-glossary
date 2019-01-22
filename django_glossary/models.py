from django.db import models
from django.urls import reverse


class Term(models.Model):
    created     = models.DateTimeField(auto_now_add=True, editable=False)
    modified    = models.DateTimeField(auto_now=True, editable=False)
    title       = models.CharField(max_length=250)
    slug        = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('django_glossary:term-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title', '-modified']


class Synonym(models.Model):
    title = models.CharField(max_length=250)
    term  = models.ForeignKey(Term, related_name="synonyms")

    def __str__(self):
        return f"{self.title} (synonym for {self.term.title})"

    def get_absolute_url(self):
        return reverse('django_glossary:term-detail', kwargs={'slug': self.term.slug})
