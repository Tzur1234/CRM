# Generated by Django 4.1.7 on 2023-02-26 21:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_category_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='description',
            field=models.TextField(default='description ...'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.userprofile'),
        ),
    ]
