# Generated by Django 4.1.7 on 2023-03-31 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='gfg_username',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_username',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hackerrank_username',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='leetcode_username',
            field=models.TextField(blank=True),
        ),
    ]