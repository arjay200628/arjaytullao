from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Project, TechStack


class TechStackModelTests(TestCase):
    def test_project_can_link_multiple_tech_stacks(self):
        python = TechStack.objects.create(name='Python')
        django = TechStack.objects.create(name='Django')
        project = Project.objects.create(
            project_name='Portfolio Website',
            description='A professional portfolio site.',
            link='https://example.com',
        )

        project.tech_stacks.add(python, django)

        self.assertEqual(project.tech_stacks.count(), 2)
        self.assertIn(python, project.tech_stacks.all())
        self.assertIn(django, project.tech_stacks.all())


class AdminAuthTests(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.superuser = self.User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='StrongPass123!',
        )
        self.regular_user = self.User.objects.create_user(
            username='regularuser',
            email='regular@example.com',
            password='StrongPass123!',
        )

    def test_superuser_can_login_and_is_redirected_to_dashboard(self):
        response = self.client.post(
            reverse('admin_login'),
            {'username': 'adminuser', 'password': 'StrongPass123!'},
            follow=True,
        )

        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_regular_user_cannot_login_to_admin_page(self):
        response = self.client.post(
            reverse('admin_login'),
            {'username': 'regularuser', 'password': 'StrongPass123!'},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, 'Only administrators can sign in')
