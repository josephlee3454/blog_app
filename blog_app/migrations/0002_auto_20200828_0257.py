# Generated by Django 3.1 on 2020-08-28 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogapp',
            name='topic',
            field=models.CharField(default='topic', max_length=30),
        ),
    ]
