# Generated by Django 4.2.4 on 2023-09-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_username_customer_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='otp',
        ),
        migrations.AddField(
            model_name='customuser',
            name='activation_code',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
