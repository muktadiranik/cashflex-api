# Generated by Django 4.0.10 on 2023-05-16 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'FAQ category',
                'verbose_name_plural': 'FAQ categories',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('discription', models.TextField(verbose_name='Discription')),
                ('website', models.URLField(verbose_name='Website')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.CreateModel(
            name='TrainingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Training type',
                'verbose_name_plural': 'Training types',
            },
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('discription', models.TextField(verbose_name='Discription')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('video', models.URLField(verbose_name='Video link')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.trainingtype', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Trainings',
            },
        ),
        migrations.CreateModel(
            name='PartnerImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='partner', verbose_name='Image')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.partner', verbose_name='Partner')),
            ],
            options={
                'verbose_name': 'Partner image',
                'verbose_name_plural': 'Partner images',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Question')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.faqcategory', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]
