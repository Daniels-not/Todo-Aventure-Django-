# Generated by Django 3.1.3 on 2021-12-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_todoitems_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitems',
            name='dateTime',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
