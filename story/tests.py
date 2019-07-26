from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User


class HomePageTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='mohit', email='mohit@sharestory.com', password='123')
        Post.objects.create(title='Hello', content='Hello, World', author=user)

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('story-home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('story-home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'story/home.html')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')

    def test_post_object(self):
        post = Post.objects.get(id=1)
        expected_object_title = f'{post.title}'
        self.assertEquals(expected_object_title, 'Hello')
        expected_object_content = f'{post.content}'
        self.assertEquals(expected_object_content, 'Hello, World')

    def test_post_list_view(self):
        response = self.client.get(reverse('story-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World')
        self.assertTemplateUsed(response, 'story/home.html')


class AboutPageTests(SimpleTestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('story-about'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('story-about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'story/about.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about/')
        self.assertContains(response, 'About Page')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/about/')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')


class NewPostTests_Before_Authentication(TestCase):
    def test_create_post_page_status_code(self):
        response = self.client.get('/post/new/')
        self.assertEquals(response.status_code, 302)

    def test_create_post_view_url_by_name(self):
        response = self.client.get(reverse('post-create'))
        self.assertEquals(response.status_code, 302)


class NewPostTests_After_Authentication(TestCase):

    def setUp(self):
        User.objects.create_user(username='mohit', email='mohit@sharestory.com', password='123')
        self.client.login(username='mohit', password='123')

    def test_create_post_page_status_code(self):
        response = self.client.get('/post/new/')
        self.assertEquals(response.status_code, 200)

    def test_create_post_view_url_by_name(self):
        response = self.client.get(reverse('post-create'))
        self.assertEquals(response.status_code, 200)

    def test_create_post_view_uses_correct_template(self):
        response = self.client.get(reverse('post-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'story/post_form.html')

    def test_csrf(self):
        response = self.client.get(reverse('post-create'))
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_create_post_with_valid_post_data(self):
        data = {
            'title': 'Test title',
            'content': 'Test content'
        }
        self.client.post(reverse('post-create'), data)
        self.assertTrue(Post.objects.exists())

    def test_create_post_with_invalid_post_data(self):
        response = self.client.post(reverse('post-create'), {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_create_post_with_empty_post_data(self):
        data = {
            'title': '',
            'content': ''
        }
        response = self.client.post(reverse('post-create'), data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Post.objects.exists())
