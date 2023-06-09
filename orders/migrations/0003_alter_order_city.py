# Generated by Django 4.1.5 on 2023-04-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_phone_no_alter_order_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(choices=[('Amritsar', 'Amritsar'), ('Bathinda', 'Bathinda'), ('Bhucho Mandi', 'Bhucho Mandi'), ('Barnala', 'Barnala'), ('Bajakhana', 'Bajakhana'), ('Dabawali', 'Dabawali'), ('Faridkot', 'Faridkot'), ('Talwandi Sabo', 'Talwandi Sabo'), ('Rampura', 'Rampura'), ('Maur Mandi', 'Maur Mandi'), ('Moga', 'Moga'), ('Jaito', 'Jaito'), ('Sunam', 'Sunam'), ('Sangrur', 'Sangrur'), ('Patiala', 'Patiala'), ('Kotakpura', 'Kotakpura'), ('Malout', 'Malout'), ('Ludhiana', 'Ludhiana'), ('Jalandhar', 'Jalandhar'), ('Kaliawali', 'Kaliawali'), ('Malerkotla', 'Malerkotla'), ('Khanna', 'Khanna'), ('Muktsar', 'Muktsar'), ('Rajpura', 'Rajpura')], max_length=100),
        ),
    ]
