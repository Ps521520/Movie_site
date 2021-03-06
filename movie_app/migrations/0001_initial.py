# Generated by Django 3.0.8 on 2020-08-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('movie_choice', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
