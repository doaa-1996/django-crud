from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class Snacks_Tests(TestCase):
    def test_snacks_page1(self):
        url = reverse('Snacks')
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(actual, expected)
    def test_page_templete1(self):
        url = reverse('Snacks')
        actual = self.client.get(url)
        expected='snacks.html'
        self.assertTemplateUsed(actual,expected) 

    def test_snacks_page2(self):
        url = reverse('snack_create')
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(actual, expected)    

    def test_page_templete2(self):
        url = reverse('snack_create')
        actual = self.client.get(url)
        expected='snack_create.html'
        self.assertTemplateUsed(actual,expected) 



    