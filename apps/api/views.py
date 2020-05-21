from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Recipe.objects.filter(owner=self.request.user)
        return queryset
    
    serializer_class = RecipeSerializer

    def create(self, request):
        return super().create(request)
    
    def update(self, request, *args, **kwargs):
        Recipe.objects.get(pk=self.kwargs['pk'])
        return super().update(request)

    def destroy(self, request, *args, **kwargs):
        Recipe.objects.get(pk=self.kwargs['pk'])
        return super().destroy(request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PublicRecipes(generics.ListAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Recipe.objects.filter(is_public=True)
        return queryset

    serializer_class = RecipeSerializer

class RecipeDetails(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Recipe.objects.filter(is_public=True)
        return queryset

    serializer_class = RecipeSerializer