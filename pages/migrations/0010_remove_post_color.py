# Generated by Django 4.2.5 on 2023-09-26 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_post_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='color',
        ),
    ]
