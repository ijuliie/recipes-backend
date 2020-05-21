from django.db import models
from apps.authentication.models import User
from multiselectfield import MultiSelectField

# Create your models here.
class Recipe(models.Model):
    Category = [
        ('breakfast', 'breakfast'),
        ('lunch', 'lunch'),
        ('dinner', 'dinner')
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_of_the_day = MultiSelectField(choices=Category)
    ingredients = models.TextField()
    instructions = models.TextField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return str(self.owner)