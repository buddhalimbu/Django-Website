# Generated by Django 3.1.1 on 2020-09-19 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogWebsite', '0012_auto_20200919_0845'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=50, null=True)),
                ('menu_url', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]