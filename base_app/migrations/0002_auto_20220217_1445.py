# Generated by Django 3.0.14 on 2022-02-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='alternativeno',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='mobile',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
