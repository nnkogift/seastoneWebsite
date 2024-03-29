# Generated by Django 2.0.7 on 2018-07-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('facebook', models.CharField(max_length=256)),
                ('twitter', models.CharField(max_length=256)),
                ('linkedin', models.CharField(max_length=256)),
                ('instagram', models.CharField(max_length=256)),
                ('interests', models.CharField(max_length=256)),
                ('extracurriculars', models.CharField(max_length=256)),
                ('department', models.CharField(choices=[('agency', 'Agency'), ('management', 'Property Management'), ('valuation', 'Valuation'), ('devt', 'Property development'), ('survey', 'Architecture and Quantity survey'), ('landscaping', 'Landscaping and Lawn-care'), ('facilities', 'Facilities management'), ('analysis', 'Investment analysis'), ('furniture', 'Furniture, Fixture and Fitting'), ('planning', 'Urban and Rural planning'), ('assesment', 'Environmental and Social Impact assessment'), ('land-survey', 'Land Survey')], max_length=64)),
            ],
            options={
                'verbose_name': 'Internship Request',
                'verbose_name_plural': 'Internship Requests',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(default='Customer', max_length=128)),
                ('testimony', models.TextField(default='Seastone is a great real estate company.')),
                ('logo', models.FileField(upload_to='')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('phoneno', models.CharField(max_length=128)),
                ('faxno', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('plot', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('facebook', models.CharField(max_length=128)),
                ('twitter', models.CharField(max_length=128)),
                ('linkedin', models.CharField(max_length=128)),
                ('pinterest', models.CharField(max_length=128)),
                ('googleplus', models.CharField(max_length=128)),
                ('instagram', models.CharField(max_length=128)),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('motto', models.TextField()),
                ('objective', models.TextField()),
                ('values', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Company details',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
    ]
