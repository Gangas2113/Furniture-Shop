# Generated by Django 4.1.5 on 2023-03-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='deliveryby',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(choices=[('bestselling', 'bestselling'), ('latest', 'latest'), ('new', 'new')], max_length=50),
        ),
    ]
