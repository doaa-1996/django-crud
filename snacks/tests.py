from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack


class test_snacks_crud(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'Doaa',
            email = 'doaaobeidat1996@gmail.com',
            password = 'doaa1996'
        )
        self.snack = Snack.objects.create(
            name = 'shawrma',
            purchaser = self.user,
            desc  = 'Shawarma is prepared from thin cuts of seasoned marinated lamb, mutton, veal, beef, chicken, or turkey. The slices are stacked on a skewer about 60 cm (20 in) high. Lamb fat may be added to provide extra fat for juiciness and flavor. A motorized spit slowly turns the stack of meat in front of a heating element, continuously roasting the outer layer. Shavings are cut off the rotating stack for serving, customarily with a long, sharp knife.[1]',
        )


    def test_snack_list(self):
        url = reverse('Snacks')
        actual_status_code = self.client.get(url).status_code
        expected=200
        self.assertEqual(actual_status_code, expected)

    def test_snack_details(self):
        expected = self.client.get(reverse('snack_details', args='1')).status_code
        actuall=200
        self.assertEqual(expected, actuall)


    def test_snack_create(self):
        expected = self.client.post(reverse("snack_create"),
            {
                "name": "zinger",
                "purchaser": self.user,
                "desc": "sandwich of fried checken",
            })

     
        self.assertEqual(expected.status_code, 200)
        self.assertContains(expected, 'zinger')
        self.assertContains(expected, 'Doaa'),
        self.assertContains(expected, 'sandwich of fried checke')

    def test_snack_update(self):
        expected = self.client.post(reverse('snack_update', args='1'), 
        {
            'name':'shawerma' ,
            "desc":'arabian dish',
        })
        self.assertContains(expected, 'shawerma')
        self.assertContains(expected, 'arabian dish')
        
   

    def test_snack_delete(self):
        expected = self.client.get(reverse("snack_delete", args="1")).status_code
        actuall=200
        self.assertEqual(expected, actuall)