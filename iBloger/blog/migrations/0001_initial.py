# Generated by Django 4.1.1 on 2022-09-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=240)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=15)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]