# Generated by Django 3.1.1 on 2020-10-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is available for purchas'), ('SOLD', 'This item cannot be purchased'), ('RESTOCKING', 'Item is on restocking')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is available for purchas'), ('SOLD', 'This item cannot be purchased'), ('RESTOCKING', 'Item is on restocking')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item is available for purchas'), ('SOLD', 'This item cannot be purchased'), ('RESTOCKING', 'Item is on restocking')], default='SOLD', max_length=10),
        ),
    ]
