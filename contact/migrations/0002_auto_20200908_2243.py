# Generated by Django 3.1 on 2020-09-08 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='contact_me',
            field=models.BooleanField(default=False),
        ),
    ]
