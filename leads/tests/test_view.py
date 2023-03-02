from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse('landing_page2'))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse('landing_page2'))
        self.assertTemplateUsed(response, 'leads/landing_page2.html')
    

