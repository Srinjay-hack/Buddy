# Generated by Django 3.2.4 on 2021-07-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210702_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
