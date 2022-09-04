from django.test import SimpleTestCase
from django.urls import reverse, resolve
from recipe.views import (MainPage,
                          DeclinePage,
                          HomePage,
                          About,
                          RecipesList,
                          MyRecipes,
                          RecipeDetail,
                          RecipeCheers,
                          RecipeCreate,
                          RecipeEdit,
                          RecipeDelete)


class TestUrls(SimpleTestCase):
    """Test urls redirect"""
    def test_mainpage_url_is_resolved(self):
        """ Test redirect to mainpage"""
        url = reverse('main')
        self.assertEqual(resolve(url).func.view_class, MainPage)

    def test_declinepage_url_is_resolved(self):
        """ Test redirect to declinepage"""
        url = reverse('decline')
        self.assertEqual(resolve(url).func.view_class, DeclinePage)

    def test_homepage_url_is_resolved(self):
        """ Test redirect to homepage"""
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePage)

    def test_aboutpage_url_is_resolved(self):
        """ Test redirect to about"""
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, About)

    def test_recipelist_url_is_resolved(self):
        """ Test redirect to recipe list"""
        url = reverse('recipes')
        self.assertEqual(resolve(url).func.view_class, RecipesList)

    def test_recipedetail_url_is_resolved(self):
        """ Test redirect to recipe detail page"""
        url = reverse('recipe_detail', args=['slugs'])
        self.assertEqual(resolve(url).func.view_class, RecipeDetail)

    def test_recipecheers_url_is_resolved(self):
        """ Test redirect to recipe detail page"""
        url = reverse('recipe_cheers', args=['slugs'])
        self.assertEqual(resolve(url).func.view_class, RecipeCheers)

    def test_myrecipes_url_is_resolved(self):
        """Test redirect to my recipes page"""
        url = reverse('myrecipes')
        self.assertEqual(resolve(url).func.view_class, MyRecipes)

    def test_recipe_create_url_is_resolved(self):
        """
        Test redirect to my recipe create page
        """
        url = reverse('recipecreate')
        self.assertEqual(resolve(url).func.view_class, RecipeCreate)

    def test_recipe_edit_url_is_resolved(self):
        """
        Test redirect to recipe edit page
        """
        url = reverse('recipeedit', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeEdit)

    def test_recipe_delete_url_is_resolved(self):
        """
        Test redirect to recipe edit page
        """
        url = reverse('recipedelete', args=['slug'])
        self.assertEqual(resolve(url).func.view_class, RecipeDelete)
