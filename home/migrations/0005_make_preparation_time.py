# Generated by Django 3.0.7 on 2020-06-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_make_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='make',
            name='preparation_time',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
