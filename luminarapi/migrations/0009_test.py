# Generated by Django 4.1.10 on 2023-07-11 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarapi', '0008_videoscreen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=300)),
                ('test_title', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('total_mark', models.PositiveIntegerField(default=100)),
                ('obtained_mark', models.PositiveIntegerField()),
            ],
        ),
    ]
