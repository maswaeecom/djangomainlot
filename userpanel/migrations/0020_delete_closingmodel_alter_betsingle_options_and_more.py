# Generated by Django 4.1.3 on 2022-11-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0019_resultnine_price_resultthreem_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClosingModel',
        ),
        migrations.AlterModelOptions(
            name='betsingle',
            options={'verbose_name_plural': 'All Bets'},
        ),
        migrations.AlterModelOptions(
            name='coderequest',
            options={'verbose_name_plural': 'Chips Requests'},
        ),
        migrations.AlterModelOptions(
            name='newlotteries',
            options={'verbose_name_plural': 'Lotteries 15 Min'},
        ),
        migrations.AlterModelOptions(
            name='newlotteriesnine',
            options={'verbose_name_plural': 'Lotteries 10 Min'},
        ),
        migrations.AlterModelOptions(
            name='newlotteriesthreem',
            options={'verbose_name_plural': 'Lotteries 3 Min'},
        ),
        migrations.AddField(
            model_name='wallet',
            name='level_earning',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=True),
        ),
    ]
