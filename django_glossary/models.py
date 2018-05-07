from django.db import models


class Term(models.Model):
    created     = models.DateTimeField(auto_now_add=True, editable=False)
    modified    = models.DateTimeField(auto_now=True, editable=False)
    title       = models.CharField(max_length=250)
    slug        = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title', '-modified']

    @models.permalink
    def get_absolute_url(self):
        return ('glossary_detail', (), {'slug': self.slug})

    def __str__(self):
        return self.title


class Synonym(models.Model):
    title = models.CharField(max_length=250)
    term  = models.ForeignKey(Term, related_name="synonyms")

    def __str__(self):
        return "{} (synonym for {})".format(self.title, self.term.title)