# Generated by Django 2.2.1 on 2019-05-16 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='condo_name',
            field=models.CharField(default='Not Provided', max_length=64),
        ),
        migrations.AddField(
            model_name='customuser',
            name='unit',
            field=models.CharField(default='Not Provided', max_length=64),
        ),
    ]
