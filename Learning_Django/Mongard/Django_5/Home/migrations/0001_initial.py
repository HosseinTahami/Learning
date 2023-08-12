# Generated by Django 4.2.3 on 2023-08-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.PositiveIntegerField()),
                ('owner', models.CharField(max_length=50)),
                ('pool', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('build_year', models.PositiveIntegerField()),
            ],
        ),
    ]
