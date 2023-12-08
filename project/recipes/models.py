from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm


class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(
        Category, related_name='recipes', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = RichTextField(blank=True, null=True)
    # description = models.TextField()
    created_by = models.ForeignKey(
        User, related_name='recipes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    STATUS = (('New', 'Yeni'),
              ('True', 'Evet'),
              ('False', 'Hayır'),)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50, blank=True)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = {'content', 'rate'}
