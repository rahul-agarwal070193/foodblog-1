# Generated by Django 3.0.7 on 2020-07-05 11:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200705_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='make',
            name='procedure',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
