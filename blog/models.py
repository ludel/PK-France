from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=250)
    summary = models.TextField(max_length=550)
    body = models.TextField()
    date = models.DateTimeField('date published', auto_now_add=True)
    author = models.CharField(max_length=100)
    url_image = models.CharField(max_length=250)

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
        self.image1.name = f'{self.name}/{self.image1.name}'
        self.image2.name = f'{self.name}/{self.image2.name}'
        self.image3.name = f'{self.name}/{self.image3.name}'

        super(Dinosaur, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
