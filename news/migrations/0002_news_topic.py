# Generated by Django 5.0.1 on 2024-01-29 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='topic',
            field=models.CharField(default='Accident', max_length=30),
            preserve_default=False,
        ),
    ]
