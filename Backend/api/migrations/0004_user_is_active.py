# Generated by Django 4.2 on 2023-04-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_disciplines_options_alter_events_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]