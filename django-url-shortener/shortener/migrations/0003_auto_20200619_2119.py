# Generated by Django 3.0.6 on 2020-06-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_shortenedurl_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='original_url',
            field=models.CharField(max_length=2048),
        ),
    ]