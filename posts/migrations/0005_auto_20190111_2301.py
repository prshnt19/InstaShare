# Generated by Django 2.1.5 on 2019-01-11 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
    ]