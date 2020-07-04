# Generated by Django 3.0.7 on 2020-07-01 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200625_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='make',
            name='thunbnail_image',
            field=models.ImageField(default='static/images/ip-3.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='make',
            name='preparation_time',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='make',
            name='serve',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
