# Generated by Django 3.2.7 on 2022-01-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_alter_reserv_creator_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv',
            name='creator_id',
            field=models.IntegerField(default=0, verbose_name='شناسه کاربر سازده'),
        ),
    ]