# Generated by Django 4.1.10 on 2023-07-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminarapi', '0007_alter_liveclass_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
