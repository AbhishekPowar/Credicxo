# Generated by Django 3.0.3 on 2020-04-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifsc_app', '0002_delete_bankdetaisl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('index', models.IntegerField(blank=True, null=True)),
                ('ifsc', models.TextField(blank=True, null=True)),
                ('bank_id', models.IntegerField(blank=True, null=True)),
                ('branch', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('district', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('bank_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bank_details',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='BankDetails',
        ),
    ]