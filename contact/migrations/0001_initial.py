# Generated by Django 3.1 on 2020-09-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('tel_number', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=254)),
                ('contact_me', models.BooleanField()),
                ('contact_me_by', models.CharField(max_length=100)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
