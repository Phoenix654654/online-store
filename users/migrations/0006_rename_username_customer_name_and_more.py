# Generated by Django 4.2.4 on 2023-09-04 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_name_customer_username_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='username',
            new_name='name',
        ),
    ]
