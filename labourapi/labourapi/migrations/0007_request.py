# Generated by Django 4.0.1 on 2022-08-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labourapi', '0006_rename_contractor_work_contractor_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
