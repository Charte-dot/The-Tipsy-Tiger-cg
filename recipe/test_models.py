from django.test import TestCase
from .models import Recipe, User


class TestModels(TestCase):
    """Test user and test recipe"""
    def setUp(self):
        user_a = User.objects.create_user(
            'user_1',
            'testuseremail@email.com',
            'my_password'
        )
        self.user_a = user_a
        user_b = User.objects.create_user(
            'user_2',
            'email@valid.com',
            'a_password'
        )
        self.user_b = user_b
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            author=user_b,
            skill='quick and easy',
            base='bourbon'
        )

    def test_recipe_gets_slug_from_title(self):
        """Tests slug is auto generated from title"""
        self.assertEqual(self.recipe.slug, 'test-recipe')

    def test_model_title_output_is_string(self):
        """Test title is a string"""
        self.assertEqual(str(self.recipe.title), 'Test Recipe')

    def test_recipe_cheers_users(self):
        """Tests number of cheers on the recipe"""
        testuser = User.objects.create_user(
            username='testuser1', password='my_password')

        testuser2 = User.objects.create_user(
            username='testuser2', password='my_next_password')

        title = Recipe.objects.create(
            title='bourbon', author=testuser)

        title.cheers.set([testuser.pk, testuser2.pk])
        self.assertEqual(title.cheers.count(), 2)
