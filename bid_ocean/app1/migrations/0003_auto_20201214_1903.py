# Generated by Django 3.1.4 on 2020-12-14 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20201214_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='intermediate',
            name='Quantity',
            field=models.IntegerField(null=True),
        ),
    ]
