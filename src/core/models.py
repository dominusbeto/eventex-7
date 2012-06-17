# coding: utf-8
from datetime import time
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)
    avatar = models.FileField(_('Avatar'), upload_to='palestrantes',
                              blank=True, null=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
            ('P', _('Telefone')),
            ('E', _('E-mail')),
            ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name=_('Palestrante'))
    kind = models.CharField(_('Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('Valor'), max_length=255)


class PeriodManager(models.Manager):
    midday = time(12)

    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = qs.order_by('start_time')
        return qs

    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.midday)
        qs = qs.order_by('start_time')
        return qs


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)

    objects = PeriodManager()

    def __unicode__(self):
        return self.title

    @property
    def slides(self):
        return self.media_set.filter(type="SL")

    @property
    def videos(self):
        return self.media_set.filter(type="YT")


class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()


class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'Youtube'),
        )

    talk = models.ForeignKey('Talk')
    type = models.CharField(max_length=2, choices=MEDIAS)
    title = models.CharField(u'Título', max_length=255, help_text=u'No caso do slideshare será usado como doc_id.')
    media_id = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)