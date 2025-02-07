# Generated by Django 2.2.1 on 2019-09-06 15:43

from django.db import migrations
import pkfrance.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='image_min',
        ),
        migrations.AddField(
            model_name='article',
            name='image_max',
            field=pkfrance.fields.ResizeImageField(default=0, size=[1100, 650], upload_to='article'),
            preserve_default=False,
        ),
    ]
