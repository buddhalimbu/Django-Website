# Generated by Django 3.1.1 on 2020-09-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogWebsite', '0007_sitelogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100, null=True)),
                ('manu_link', models.URLField(max_length=100)),
            ],
        ),
    ]
