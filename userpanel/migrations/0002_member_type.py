# Generated by Django 4.0.4 on 2022-09-20 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
