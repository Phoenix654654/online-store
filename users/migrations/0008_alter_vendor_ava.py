# Generated by Django 4.2.4 on 2023-09-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_vendor_otp_customuser_activation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='ava',
            field=models.ImageField(default='default_profile.jpg', upload_to='user/'),
        ),
    ]
