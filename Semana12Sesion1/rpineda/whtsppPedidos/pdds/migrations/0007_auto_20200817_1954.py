# Generated by Django 3.1 on 2020-08-18 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdds', '0006_auto_20200817_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='docmento',
            new_name='documento',
        ),
    ]
