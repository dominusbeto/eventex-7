# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Speaker
from .models import Contact

class HomepageTest(TestCase):
    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'index.html')


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name="Henrique Bastos",
                               slug="henrique-bastos",
                               url="http://henriquebastos.net",
                               description="Passionate software developer!",
                               avatar="")
        self.speaker.save()

    def test_create(self):
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        self.assertEqual(u"Henrique Bastos", unicode(self.speaker))


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name="Henrique Bastos",
                                              slug="henrique-bastos",
                                              url="http://henriquebastos.net",
                                              description="Passionate software developer!",
                                              avatar="")
    def test_create_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='henrique@bastos.net')
        self.assertEqual(1, contact.pk)

    def test_create_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P', value='21-96186180')
        self.assertEqual(1, contact.pk)

    def test_create_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F', value='21-98989898')
        self.assertEqual(1, contact.pk)



class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name="Henrique Bastos",
                               slug="henrique-bastos",
                               url="http://henriquebastos.net",
                               description="Passionate software developer!",
                               avatar="")
        self.resp = self.client.get(reverse('core:speaker_detail', kwargs={'slug': 'henrique-bastos'}))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_speaker_in_context(self):
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)
