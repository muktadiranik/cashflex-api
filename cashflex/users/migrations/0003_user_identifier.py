# Generated by Django 4.0.10 on 2023-03-29 09:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_first_name_user_last_name_user_uuid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identifier',
            field=models.CharField(default=django.utils.timezone.now, max_length=40, unique=True),
            preserve_default=False,
        ),
    ]
