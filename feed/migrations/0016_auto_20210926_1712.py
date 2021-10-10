# Generated by Django 3.2.6 on 2021-09-26 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0015_alter_post_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='CompanyName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.CharField(choices=[('Cse', 'Cse'), ('Ece', 'Ece'), ('Eee', 'Eee'), ('IS', 'IS'), ('Mechanical', 'Mechanical'), ('Civil', 'Civil'), ('Chemical', 'Chemical')], default='Cse', max_length=20),
        ),
    ]
