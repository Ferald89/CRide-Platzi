# Generated by Django 2.0.10 on 2020-05-10 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_auto_20200510_1813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='is_acive',
            new_name='is_active',
        ),
    ]
