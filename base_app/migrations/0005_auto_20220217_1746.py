# Generated by Django 3.0.14 on 2022-02-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_auto_20220217_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='dateofbirth',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]