# Generated by Django 4.0.6 on 2024-05-20 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0012_musica_letra'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
