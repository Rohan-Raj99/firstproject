# Generated by Django 3.2.9 on 2021-11-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='mail',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='result',
            name='stuname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
