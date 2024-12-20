# Generated by Django 5.1.3 on 2024-12-06 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mission_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('pay', models.FloatField(default=0)),
                ('summary', models.TextField(blank=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.location')),
                ('participants', models.ManyToManyField(related_name='missions', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reports.mission_type')),
            ],
        ),
    ]
