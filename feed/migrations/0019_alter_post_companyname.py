# Generated by Django 3.2.6 on 2021-10-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0018_alter_post_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='CompanyName',
            field=models.CharField(max_length=50),
        ),
    ]
