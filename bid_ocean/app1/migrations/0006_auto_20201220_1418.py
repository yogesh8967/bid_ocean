# Generated by Django 3.1.4 on 2020-12-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_dish_dish_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='Ph_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
