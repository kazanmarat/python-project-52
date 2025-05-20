from django.test import TestCase
from accounts.models import CustomUser
from .models import Status
from django.urls import reverse


class StatusTest(TestCase):
    fixtures = ['statuses/fixtures.json', 'statuses/fixtures_user.json',]

    @classmethod
    def setUpTestData(cls):
        cls.initial_status_count = Status.objects.count()
        cls.user = CustomUser.objects.get(pk=1)
        cls.status = Status.objects.get(pk=1)
        cls.status_list_url = reverse("status_list")
        
    def setUp(self):
        self.client.force_login(self.user)

    def test_status_list(self):
        response = self.client.get(self.status_list_url)
        statuses = response.context["statuses"]
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.status_list_url)
        self.assertTrue(len(statuses) == self.initial_status_count)

    def test_status_create(self):
        # create status
        create_url = reverse("status_create")
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        status_data = {'name': 'test status 3'}
        response = self.client.post(create_url, status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.status_list_url)

        # check added status
        response = self.client.get(self.status_list_url)
        statuses = response.context["statuses"]
        self.assertContains(response, 'test status 3')
        self.assertTrue(len(statuses) == self.initial_status_count + 1)

    def test_status_update(self):
        old_status_name = self.status.name
        new_status_name = 'new test status'
        update_url = reverse("status_update", kwargs={"pk": self.status.id})

        # update status
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        status_data = {'name': new_status_name}
        response = self.client.post(update_url, status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.status_list_url)

        # check updated status
        response = self.client.get(self.status_list_url)
        self.assertContains(response, new_status_name)
        self.assertNotContains(response, old_status_name)

    def test_status_delete(self):
        status_name = self.status.name
        delete_url = reverse("status_delete", kwargs={"pk": self.status.id})

        # delete status
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.status_list_url)

        # check deleted status
        response = self.client.get(self.status_list_url)
        statuses = response.context["statuses"]
        self.assertTrue(len(statuses) == self.initial_status_count - 1)
        self.assertNotContains(response, status_name)
