from django.db import models

class Term(models.Model):
    title       = models.CharField(max_length=250)
    slug        = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    @models.permalink
    def get_absolute_url(self):
       return ('glossary_detail', (), {'slug': self.slug})

    def __unicode__(self):
        return unicode(self.title)

class Synonym(models.Model):
    title = models.CharField(max_length=250)
    term  = models.ForeignKey(Term, related_name="synonyms")

    def __unicode__(self):
        return u"%s (synonym for %s)" % (self.title, self.term.title)
