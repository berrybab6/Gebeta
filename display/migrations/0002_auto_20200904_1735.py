# Generated by Django 3.1 on 2020-09-04 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chief',
            old_name='ch_img',
            new_name='chief_img',
        ),
        migrations.RenameField(
            model_name='chief',
            old_name='ch_name',
            new_name='chief_name',
        ),
    ]
