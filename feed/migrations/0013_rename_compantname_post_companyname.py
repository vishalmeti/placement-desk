# Generated by Django 3.2.6 on 2021-09-26 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_rename_dificulty_post_difficulty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='CompantName',
            new_name='CompanyName',
        ),
    ]
