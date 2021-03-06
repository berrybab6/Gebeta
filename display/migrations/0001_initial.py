# Generated by Django 3.1 on 2020-09-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chief',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('ch_img', models.ImageField(upload_to='')),
                ('exprience', models.PositiveIntegerField()),
                ('role', models.CharField(max_length=200)),
                ('awards_num', models.PositiveIntegerField(null=True)),
                ('award_types', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=100)),
                ('F_desc', models.TextField()),
                ('F_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
