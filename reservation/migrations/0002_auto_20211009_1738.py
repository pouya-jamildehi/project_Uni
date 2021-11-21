# Generated by Django 3.2.7 on 2021-10-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
        ('art_artist', '0001_initial'),
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserv',
            name='art',
            field=models.ManyToManyField(to='art_artist.Art', verbose_name='انتخاب تصویر'),
        ),
        migrations.AddField(
            model_name='reserv',
            name='wall',
            field=models.ManyToManyField(to='wall.Wall', verbose_name='انتخاب دیوار'),
        ),
    ]
