# Generated by Django 4.1.7 on 2023-02-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_mymodel_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
