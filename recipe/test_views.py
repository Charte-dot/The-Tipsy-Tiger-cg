from django.test import TestCase, Client
from django.urls import reverse
from recipe.models import Recipe, User


class TestView(TestCase):
    """Test views"""

    def setUp(self):
        """Create a test user"""
        self.client = Client()
        self.user_a = User(username='testuser', email='testuser@email.com')
        self.user_a.set_password('my_password')
        self.client.login(username='testuser', password='my_password')
        self.user_a.save()
        user_b = User.objects.create_user('user_2'
                                          'email@invaild.com'
                                          'a_password')
        self.user_b = user_b

        # recipe test

        self.recipe = Recipe.objects.create(
            title='test recipe',
            author=self.user_a,)
        self.recipe_detail_url = reverse('recipe_detail', args=['test-recipe'])
        self.recipecreate_url = reverse('recipecreate')

    def test_get_decline_page(self):
        """Test decline page ressponse is 200"""
        response = self.client.get('/decline/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'decline.html')

    def test_get_homelist(self):
        """Test home response is 200"""
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about_page(self):
        """Test about page response is 200"""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_access_to_recipe_detail_page_requires_login(self):
        """Test logged in user can access recipe detail page"""
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_access_to_recipe_cheers_requires_login(self):
        """Test that the logged in user can view recipe details"""
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_access_to_edit_recipe_requires_login(self):
        """Test that the logged in user can edit recipe details"""
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_access_to_create_recipe_requires_login(self):
        """Test that the logged in user can create recipe details"""
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)

    def test_access_to_delete_recipe_requires_login(self):
        """Test that the logged in user can delete recipe details"""
        response = self.client.get(self.recipe_detail_url)
        self.assertEqual(response.status_code, 302)
