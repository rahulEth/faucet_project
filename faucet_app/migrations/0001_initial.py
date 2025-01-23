# Generated by Django 4.2 on 2025-01-23 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_address', models.CharField(max_length=42)),
                ('transaction_hash', models.CharField(max_length=66)),
                ('status', models.BooleanField(default=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faucet_app_transaction',
                'managed': True,
            },
        ),
    ]
