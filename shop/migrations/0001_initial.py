# Generated by Django 4.1.5 on 2023-03-07 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='blog/')),
                ('postby', models.CharField(max_length=50)),
                ('poston', models.DateField()),
            ],
            options={
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
