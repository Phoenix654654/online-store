# Generated by Django 4.2.4 on 2023-09-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_vendor_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='name',
            new_name='username',
        ),
    ]
