# Generated by Django 3.2.4 on 2021-07-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_caller_estimated_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caller',
            name='list_file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]