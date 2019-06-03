from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    summary = models.TextField(max_length=550)
    body = models.TextField()
    date = models.DateField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        self.image.name = f'article/{self.image.name}'

        super(Article, self).save(*args, **kwargs)

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
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()

    def save(self, *args, **kwargs):
        self.image1.name = f'dinosaur/{self.name}/{self.image1.name}'
        self.image2.name = f'dinosaur/{self.name}/{self.image2.name}'
        self.image3.name = f'dinosaur/{self.name}/{self.image3.name}'

        super(Dinosaur, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Fact(models.Model):
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField('date published', auto_now_add=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        self.image.name = f'fact/{self.image.name}'

        super(Fact, self).save(*args, **kwargs)
