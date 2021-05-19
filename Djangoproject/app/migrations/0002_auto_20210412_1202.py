# Generated by Django 3.2 on 2021-04-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrecord',
            name='Email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userrecord',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userrecord',
            name='Password',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
