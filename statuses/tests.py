from django.test import TestCase
from accounts.models import CustomUser
from .models import Status
from django.urls import reverse


class StatusTest(TestCase):
    fixtures = ['statuses/fixtures.json', 'statuses/fixtures_user.json',]

    def setUp(self):
        user = CustomUser.objects.get(pk=1)
        self.client.get(reverse("login"))
        self.client.force_login(user)

    def test_status_list(self):
        status_count = Status.objects.count()
        status_list_url = reverse("status_list")
        response = self.client.get(status_list_url)
        statuses = response.context["statuses"]
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(status_list_url)
        self.assertTrue(len(statuses) == status_count)

    def test_status_create(self):
        initial_count = Status.objects.count()
        status_list_url = reverse("status_list")
        create_url = reverse("status_create")

        # create status
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        status_data = {'name': 'test status 3'}
        response = self.client.post(create_url, status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, status_list_url)

        # check added status
        response = self.client.get(status_list_url)
        statuses = response.context["statuses"]
        self.assertTrue(len(statuses) == initial_count + 1)

    def test_status_update(self):
        status = Status.objects.get(pk=1)
        old_status_name = status.name
        new_status_name = 'new test status'
        update_url = reverse("status_update", kwargs={"pk": status.id})
        status_list_url = reverse("status_list")

        # update status
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        status_data = {'name': new_status_name}
        response = self.client.post(update_url, status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, status_list_url)

        # check updated status
        response = self.client.get(status_list_url)
        self.assertContains(response, new_status_name)
        self.assertNotContains(response, old_status_name)

    def test_status_delete(self):
        status = Status.objects.get(pk=1)
        status_name = status.name
        initial_count = Status.objects.count()
        delete_url = reverse("status_delete", kwargs={"pk": status.id})
        status_list_url = reverse("status_list")

        # delete status
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, status_list_url)

        # check deleted status
        response = self.client.get(status_list_url)
        statuses = response.context["statuses"]
        self.assertTrue(len(statuses) == initial_count - 1)
        self.assertNotContains(response, status_name)
