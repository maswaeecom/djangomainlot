# Generated by Django 4.1.3 on 2022-11-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0020_delete_closingmodel_alter_betsingle_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='widhdraw_requests',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
