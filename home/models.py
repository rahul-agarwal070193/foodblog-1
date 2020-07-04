from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils.timezone import now
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
difficult = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('difficult', 'difficult'),
    ('expert', 'expert'),
)
type = (
    ('vegetarian', 'vegetarian'),
    ('non', 'non-vegetarian'),
)
menu_type = (
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Quickbite', 'Quickbite'),
    ('Dinner', 'Dinner'),
    ('Dessert', 'Dessert'),
    ('Beverage', 'Beverage'),


)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    thumbnail_image = models.ImageField(
        upload_to="image/Profile", blank=True, null=True)
    bio = models.TextField()
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    snapchat_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user)


class make(models.Model):

    recipe_name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(default=now)
    short_description = models.CharField(max_length=300)
    thumbnail_image = models.ImageField(
        upload_to="image/")
    Recipe_video = models.FileField(upload_to="videos/")
    difficulty = models.CharField(
        max_length=10,
        choices=difficult, default='easy')
    food_type = models.CharField(
        max_length=15,
        choices=type, default='vegetarian')
    serve = models.PositiveSmallIntegerField()
    menu = models.CharField(
        max_length=15,
        choices=menu_type, default='Dessert')
    ingredients = RichTextField()
    procedure = RichTextField()
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)
    preparation_time = models.PositiveIntegerField()
    comman = models.CharField(blank=True, null=True, max_length=500)

    def __str__(self):
        return self.recipe_name+"|"+str(self.author)

    def get_absolute_url(self):
        return reverse('all_post')
