# Generated by Django 2.0.2 on 2018-04-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_theater_county'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theater',
            name='county',
        ),
        migrations.AddField(
            model_name='theater',
            name='city',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]