# Generated by Django 3.2.15 on 2023-05-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_socialmedialink'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('youtube', 'Youtube')], max_length=100, unique=True, verbose_name='Platform')),
                ('url', models.URLField(verbose_name='Link')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Medias',
            },
        ),
        migrations.DeleteModel(
            name='SocialMediaLink',
        ),
    ]
