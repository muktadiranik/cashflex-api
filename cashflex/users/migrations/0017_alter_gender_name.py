# Generated by Django 4.0.10 on 2023-04-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_gender_role_user_role_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
