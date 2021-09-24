# Generated by Django 3.2.7 on 2021-09-24 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_alter_user_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]