# Generated by Django 2.2.1 on 2019-09-07 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190906_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinosaur',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(),
        ),
    ]
