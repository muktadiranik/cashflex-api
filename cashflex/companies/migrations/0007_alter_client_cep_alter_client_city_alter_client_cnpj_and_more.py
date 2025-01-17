# Generated by Django 4.0.10 on 2023-04-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_client_user_email_client_user_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='cep',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='client',
            name='cnpj',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='client',
            name='complement',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Complement'),
        ),
        migrations.AlterField(
            model_name='client',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='client',
            name='employee_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Number of Employees'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name of Company'),
        ),
        migrations.AlterField(
            model_name='client',
            name='razao_social',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Razao Social'),
        ),
        migrations.AlterField(
            model_name='client',
            name='schema_name',
            field=models.CharField(db_index=True, max_length=63, unique=True, verbose_name='Schema Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='client',
            name='street_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Name'),
        ),
        migrations.AlterField(
            model_name='client',
            name='street_number',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Street Number'),
        ),
        migrations.AlterField(
            model_name='client',
            name='team',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Team'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='HR email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_password',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='HR password'),
        ),
        migrations.AlterField(
            model_name='client',
            name='user_username',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='HR username'),
        ),
    ]
