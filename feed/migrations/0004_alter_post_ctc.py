# Generated by Django 3.2.6 on 2021-09-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20210925_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ctc',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
