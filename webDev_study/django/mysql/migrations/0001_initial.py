# Generated by Django 3.0.7 on 2020-06-25 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(db_column='uid', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('rqtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['username'],
            },
        ),
    ]
