# Generated by Django 4.2.4 on 2023-09-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_alter_customer_ava_alter_vendor_ava'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='ava',
            field=models.ImageField(default='default_profile.jpg', upload_to='user/'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='ava',
            field=models.ImageField(default='default_profile.jpg', upload_to='user/'),
        ),
    ]