# Generated by Django 3.0.4 on 2020-09-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('veh', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
    ]
