# Generated by Django 3.1.1 on 2021-02-09 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('responsive', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colours',
            old_name='colourname',
            new_name='colourcode',
        ),
    ]
