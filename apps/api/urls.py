from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, PublicRecipes, RecipeDetails

router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')

custom_urlpatterns = [
    url(r'^publicrecipes', PublicRecipes.as_view(), name='publicrecipes'),
     url(r'^publicrecipes/(?P<pk>\d+)/$', RecipeDetails.as_view(), name='recipedetails')
]

urlpatterns = router.urls
urlpatterns += custom_urlpatterns