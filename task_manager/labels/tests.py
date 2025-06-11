from django.test import TestCase
from django.urls import reverse

from task_manager.accounts.models import CustomUser

from .models import Label


class LabelTest(TestCase):
    fixtures = [
        "fixtures_labels.json",
        "fixtures_accounts.json",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.initial_count = Label.objects.count()
        cls.user = CustomUser.objects.get(pk=1)
        cls.label = Label.objects.get(pk=1)
        cls.list_url = reverse("label_list")

    def setUp(self):
        self.client.force_login(self.user)

    def test_label_list(self):
        response = self.client.get(self.list_url)
        labels = response.context["labels"]
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.list_url)
        self.assertTrue(len(labels) == self.initial_count)

    def test_label_create(self):
        # create label
        create_url = reverse("label_create")
        response = self.client.get(create_url)
        self.assertEqual(response.status_code, 200)
        label_data = {"name": "test label 3"}
        response = self.client.post(create_url, label_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)

        # check added label
        response = self.client.get(self.list_url)
        labels = response.context["labels"]
        self.assertContains(response, "test label 3")
        self.assertTrue(len(labels) == self.initial_count + 1)

    def test_label_update(self):
        old_name = self.label.name
        new_name = "new test label"
        update_url = reverse("label_update", kwargs={"pk": self.label.id})

        # update label
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 200)
        label_data = {"name": new_name}
        response = self.client.post(update_url, label_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)

        # check updated label
        response = self.client.get(self.list_url)
        self.assertContains(response, new_name)
        self.assertNotContains(response, old_name)

    def test_label_delete(self):
        label_name = self.label.name
        delete_url = reverse("label_delete", kwargs={"pk": self.label.id})

        # delete label
        response = self.client.get(delete_url)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)

        # check deleted label
        response = self.client.get(self.list_url)
        labels = response.context["labels"]
        self.assertTrue(len(labels) == self.initial_count - 1)
        self.assertNotContains(response, label_name)
