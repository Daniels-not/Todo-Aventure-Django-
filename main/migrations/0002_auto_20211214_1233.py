# Generated by Django 3.1.3 on 2021-12-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
