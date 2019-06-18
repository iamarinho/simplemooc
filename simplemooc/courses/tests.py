from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.conf import settings
#não funciona mais from django.core.urlresolvers import reverse

from .models import Course

#class ContactCourseTestCase(TestCase):
 #   def setUp(self):
  #    self.course = Course.objects.create(name='Django', slug='django')

   # def tearDown(self):
    #    self.course.delete()
    
   # def test_fields_required_not_filled(self):
    #    data={'name': '', 'email': '', 'message': ''}
     #   client = Client()
      #  path = reverse('courses:details', args=[self.course.slug])
       # response = client.post(path, data)
        #self.assertContains(response, 'Form','name', 'Preencha este campo', 200)
        #self.assertFormError(response, 'Form','email', 'Preencha este campo', msg_prefix='Campo email exibiu o erro de obrigatoriedade')
        #self.assertFormError(response, 'Form','message', 'Preencha este campo', msg_prefix='Campo message exibiu o erro de obrigatoriedade')

  #  def test_contact_form_success(self):           
   #      data={'name': 'Iasmy', 'email': 'iasmy@test.com', 'message': 'oi'}
    #     client = Client()
     #    path = reverse('courses:details', args=[self.course.name])
      #   response = client.post(path, data)
       #  self.assertEqual(len(mail.outbox), 1)
         #self.assertEqual(mail.outbox[0].to, [settings.CONTACT_EMAIL])
