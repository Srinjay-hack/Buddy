# Generated by Django 3.2.4 on 2021-07-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210702_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assistant',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='caller',
            name='email',
            field=models.CharField(max_length=20),
        ),
    ]
