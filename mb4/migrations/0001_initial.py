# Generated by Django 3.2.6 on 2021-08-26 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reeks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='reeksfotos/')),
                ('uitleg', models.TextField()),
                ('datum', models.DateField(auto_now_add=True)),
                ('soort', models.CharField(max_length=100)),
                ('onderwerp', models.CharField(max_length=100)),
                ('glob_moeilkhgr', models.CharField(choices=[('*', 'Easy'), ('**', 'Doable'), ('***', 'Hard'), ('****', 'Die hard')], max_length=4)),
                ('glob_strtijd', models.IntegerField()),
                ('vereiste_level', models.CharField(default='MB1', max_length=50)),
                ('nodig_materiaal', models.CharField(max_length=200)),
                ('joke', models.ImageField(blank=True, null=True, upload_to='reeksfotos/')),
                ('website_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Reeks',
                'verbose_name_plural': 'Reeksen',
            },
        ),
        migrations.CreateModel(
            name='Opgave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onderwerp', models.CharField(max_length=100)),
                ('opg_titel', models.CharField(blank=True, max_length=100)),
                ('opl', models.IntegerField()),
                ('moeilkhgr', models.IntegerField()),
                ('strtijd', models.IntegerField()),
                ('reeks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mb4.reeks')),
            ],
            options={
                'verbose_name': 'Opgave',
                'verbose_name_plural': 'Opgaven',
            },
        ),
        migrations.CreateModel(
            name='Oefening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antwoord', models.IntegerField(blank=True)),
                ('delta', models.IntegerField()),
                ('oef_datum', models.DateTimeField(verbose_name='datum_gemaakt')),
                ('opgave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mb4.opgave')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Oefening',
                'verbose_name_plural': 'Oefeningen',
            },
        ),
    ]
