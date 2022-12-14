# Generated by Django 4.1.3 on 2022-12-03 01:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0026_alter_newlotteries_id_alter_newlotteriesnine_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buychips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=100)),
                ('hash', models.CharField(max_length=200)),
                ('fromaddress', models.CharField(max_length=200)),
                ('toaddress', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('chips', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
