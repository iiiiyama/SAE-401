# Generated by Django 4.2.2 on 2023-06-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybank', '0004_account_nom_compte_alter_account_num_compte'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='adresse',
        ),
    ]