# Generated by Django 3.1.4 on 2023-02-22 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_remove_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_organisor',
            field=models.BooleanField(default=True),
        ),
    ]
