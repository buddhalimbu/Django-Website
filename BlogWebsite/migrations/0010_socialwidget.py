# Generated by Django 3.1.1 on 2020-09-19 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogWebsite', '0009_auto_20200918_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=100, null=True)),
                ('social_link', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
