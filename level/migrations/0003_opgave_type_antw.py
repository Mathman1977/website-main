# Generated by Django 3.2.6 on 2021-08-29 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0002_excercice'),
    ]

    operations = [
        migrations.AddField(
            model_name='opgave',
            name='type_antw',
            field=models.CharField(default='input_antw', max_length=50),
        ),
    ]
