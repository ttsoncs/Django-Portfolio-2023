# Generated by Django 4.2.5 on 2023-09-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0003_blog_delete_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="cover",
            field=models.ImageField(blank=True, upload_to="covers/"),
        ),
    ]
