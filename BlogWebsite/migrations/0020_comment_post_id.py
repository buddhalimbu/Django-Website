# Generated by Django 3.1.1 on 2020-09-27 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BlogWebsite', '0019_auto_20200926_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogWebsite.blogpost'),
        ),
    ]
