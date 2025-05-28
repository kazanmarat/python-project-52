from django.test import TestCase
from .models import CustomUser
from django.urls import reverse


class CustomUserTest(TestCase):
    fixtures = ['fixtures_accounts.json']

    @classmethod
    def setUpTestData(cls):
        cls.initial_count = CustomUser.objects.count()
        cls.user = CustomUser.objects.get(pk=1)
        cls.list_url = reverse("user_list")
        
    def setUp(self):
        self.client.force_login(self.user)

    def test_user_list(self):
        response = self.client.get(self.list_url)
        users = response.context["users"]
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.list_url)
        self.assertTrue(len(users) == self.initial_count)

    def test_user_create(self):
        create_url = reverse("user_create")
        login_url = reverse("login")

        # post user data with redirect on login page
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        user_data = {
            'first_name': 'testname2',
            'last_name': 'testname2',
            'username': 'testuser102',
            'password1': 'testpass12345',
            'password2': 'testpass12345',
        }
        response = self.client.post(create_url, user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, login_url)

        # check added user
        response = self.client.get(self.list_url)
        users = response.context["users"]
        self.assertTrue(len(users) == self.initial_count + 1)
        self.assertContains(response, user_data['username'])

    def test_user_update(self):
        update_url = reverse("user_update", kwargs={"pk": self.user.id})
        old_name = self.user.username
        new_name = 'testusername100'

        # post updated data
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        updated_data = {
            'username': new_name,
            'password1': 'testpass12345',
            'password2': 'testpass12345',
        }
        response = self.client.post(update_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)

        # check updated data
        response = self.client.get(self.list_url)
        self.assertContains(response, new_name)
        self.assertNotContains(response, old_name)

    def test_user_delete(self):
        delete_url = reverse("user_delete", kwargs={"pk": self.user.id})
        username = self.user.username

        # get delete page
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        # post delete page
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)

        # check deleted user
        response = self.client.get(self.list_url)
        users = response.context["users"]
        self.assertTrue(len(users) == self.initial_count - 1)
        self.assertNotContains(response, username)
