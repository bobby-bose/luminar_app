# Generated by Django 4.1.10 on 2023-07-11 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarapi', '0003_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
