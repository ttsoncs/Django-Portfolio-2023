# Generated by Django 4.2.5 on 2023-09-25 13:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0004_blog_cover"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Blog",
            new_name="Post",
        ),
    ]
