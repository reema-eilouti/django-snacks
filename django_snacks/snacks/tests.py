from django.test import TestCase

# Create your tests here.

from django.test import SimpleTestCase
from django.urls import reverse

class thingsTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templete(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_templete(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'about.html')
        self.assertTemplateUsed(response, 'base.html')


class snacks_tests(TestCase):

    def test_snack_list(self):

        url = reverse('snack_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code , 200)
        
        self.assertTemplateUsed(response, 'snack_list.html')



    def test_snack_create(self):

        url = reverse('snack_create')

        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'base.html')

        self.assertTemplateUsed(response, 'snack_create.html')



    # def test_snack_update(self):

    #     url = reverse('snack_update', args = '1')

    #     response = self.client.get(url)

    #     self.assertEquals(response.status_code, 200)

    #     self.assertTemplateUsed(response, 'base.html')

    #     self.assertTemplateUsed(response, 'snack_update.html')



    # def test_snack_delete(self):

    #     url = reverse('snack_delete', args = '1')

    #     response = self.client.get(url)

    #     self.assertEquals(response.status_code, 200)

    #     self.assertTemplateUsed(response, 'base.html')

    #     self.assertTemplateUsed(response, 'snack_delete.html')