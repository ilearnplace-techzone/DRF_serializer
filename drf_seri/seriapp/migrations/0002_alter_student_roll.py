# Generated by Django 3.2.5 on 2021-10-22 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seriapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(),
        ),
    ]
