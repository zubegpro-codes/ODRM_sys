# Generated by Django 3.2.7 on 2023-08-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_report_rimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='report',
            name='Rimg',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
