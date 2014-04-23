import os

import orm.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'orm.settings'

from django.db import models


class PagecountURL(models.Model):
    url = models.CharField(max_length=255, null=False, unique=True)
    time = models.DateTimeField(null=False)
    retrieved = models.BooleanField(null=False, default=False)

    def __unicode__(self):
        return u"<PagecountURL: %s>" % self.url

    def __str__(self):
        return str(self.__unicode__())


class Page(models.Model):
    title = models.CharField(max_length=255, null=False)
    project = models.CharField(max_length=255, null=False)

    def __unicode__(self):
        return u"<Page: %s/%s>" % (self.title, self.project)

    def __str__(self):
        return str(self.__unicode__())


class Pagecount(models.Model):
    pagecount_url = models.ForeignKey(PagecountURL, null=False)
    page = models.ForeignKey(Page, null=False)
    count = models.IntegerField(null=False)

    def __unicode__(self):
        return u"<Pagecount: %s>" % self.id

    def __str__(self):
        return str(self.__unicode__())
