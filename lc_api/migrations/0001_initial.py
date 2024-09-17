# Generated by Django 5.1.1 on 2024-09-14 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_number', models.IntegerField()),
                ('contest_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LeetcodeProblemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('score', models.IntegerField()),
                ('link', models.URLField()),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lc_api.contest')),
            ],
        ),
    ]
