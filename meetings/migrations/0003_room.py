# Generated by Django 4.0.4 on 2022-05-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_meeting_duration_meeting_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('floor_number', models.IntegerField(max_length=100)),
                ('room_number', models.IntegerField(max_length=1000)),
            ],
        ),
    ]