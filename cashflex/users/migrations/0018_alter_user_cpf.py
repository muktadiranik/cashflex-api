# Generated by Django 4.0.10 on 2023-04-08 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_gender_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='CPF'),
        ),
    ]