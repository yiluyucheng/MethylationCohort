# Generated by Django 4.0.5 on 2022-06-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cohort', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GsmInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.CharField(max_length=256, verbose_name='ID')),
                ('age', models.FloatField(verbose_name='Age')),
                ('gender', models.CharField(max_length=20, verbose_name='Gender')),
                ('source_date', models.CharField(max_length=15, verbose_name='Sourcedate')),
                ('race', models.CharField(max_length=20, verbose_name='Race')),
                ('source', models.CharField(max_length=40, verbose_name='Source')),
                ('group', models.CharField(max_length=40, verbose_name='Group')),
                ('disease', models.CharField(max_length=20, verbose_name='Disease')),
                ('series', models.CharField(max_length=30, verbose_name='Series')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Add_date')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='Update_date')),
            ],
            options={
                'verbose_name': 'GSM Info',
            },
        ),
    ]
