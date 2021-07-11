# Generated by Django 3.2.4 on 2021-07-11 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_caller_estimated_amount'),
        ('caller', '0002_auto_20210709_0642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('assistant_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='accounts.assistant')),
                ('is_connected', models.BooleanField(default=False)),
            ],
            bases=('accounts.assistant',),
        ),
    ]
