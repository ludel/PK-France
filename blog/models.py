from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from pkfrance.fields import ResizeImageField


class Article(models.Model):
    title = models.CharField(max_length=250)
    summary = models.TextField(max_length=550)
    body = models.TextField()
    date = models.DateField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = ResizeImageField(size=[700, 400], upload_to='article')

    def get_absolute_url(self):
        return reverse('article', args=[self.pk])

    def __str__(self):
        return f'{self.pk} - {self.title}'


class Dinosaur(models.Model):
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=20)
    period = models.CharField(max_length=20)
    classification = models.CharField(max_length=200)
    description = models.TextField()
    in_game = models.TextField()
    image1 = ResizeImageField(size=[700, 400], upload_to='dinosaur')
    image2 = ResizeImageField(size=[700, 400], upload_to='dinosaur')
    image3 = ResizeImageField(size=[700, 400], upload_to='dinosaur')

    def get_absolute_url(self):
        return reverse('dinosaur', args=[self.pk])

    def __str__(self):
        return self.name


class Fact(models.Model):
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField('date published', auto_now_add=True)
    image = ResizeImageField(size=[350, 200], upload_to='fact')

    def get_absolute_url(self):
        return reverse('fact', args=[self.pk])
