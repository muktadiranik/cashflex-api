# Generated by Django 4.0.10 on 2023-04-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
