from django.test import TestCase
from .models import CustomUser
from django.urls import reverse


class CustomUserTest(TestCase):
    fixtures = ['accounts/fixtures.json']

    def test_user_list(self):
        user_count = CustomUser.objects.count()
        user_list_url = reverse("user_list")
        response = self.client.get(user_list_url)
        users = response.context["users"]
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(users) == user_count)

    def test_user_create(self):
        user_signup_url = reverse("create")
        user_login_url = reverse("login")
        user_list_url = reverse("user_list")
        user_count = CustomUser.objects.count()

        # get sign up page and post user data with redirect on login page
        response = self.client.get(user_signup_url)
        self.assertEqual(response.status_code, 200)
        user_data = {
            'first_name': 'testname2',
            'last_name': 'testname2',
            'username': 'testuser102',
            'password1': 'testpass12345',
            'password2': 'testpass12345',
        }
        response = self.client.post(user_signup_url, user_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, user_login_url)

        # check append user
        response = self.client.get(user_list_url)
        users = response.context["users"]
        self.assertTrue(len(users) == user_count + 1)

    def test_user_update(self):
        user = CustomUser.objects.get(pk=1)
        update_url = reverse("user_update", kwargs={"pk": user.id})
        user_list_url = reverse("user_list")
        login_url = reverse('login')

        # try update and get redirect to login
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(login_url)

        # login
        self.client.force_login(user)
        
        # get update page
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)

        # post update data
        updated_data = {
            "username": "testusername100",
            'password': 'testpass12345',
        }
        response = self.client.post(update_url, updated_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, user_list_url)

        # check updated data
        response = self.client.get(user_list_url)
        self.assertContains(response, "testusername100")
        self.assertNotContains(response, "testuser100")

    def test_user_delete(self):
        user = CustomUser.objects.get(pk=1)
        user_count = CustomUser.objects.count()
        delete_url = reverse("user_delete", kwargs={"pk": user.id})
        user_list_url = reverse("user_list")
        login_url = reverse('login')

        # try delete and get redirect to login
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(login_url)

        # login
        self.client.force_login(user)
        
        # get delete page
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)

        # post delete
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, user_list_url)

        # check delete user
        response = self.client.get(user_list_url)
        users = response.context["users"]
        self.assertTrue(len(users) == user_count - 1)
