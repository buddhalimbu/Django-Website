# Generated by Django 3.1.1 on 2020-09-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogWebsite', '0021_comment_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
