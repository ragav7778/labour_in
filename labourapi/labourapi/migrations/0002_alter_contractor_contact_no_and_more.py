# Generated by Django 4.0.1 on 2022-08-25 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labourapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='contact_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='email_id1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='labour',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='labour',
            name='height',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='age',
            field=models.PositiveBigIntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='height',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='worker',
            name='weight',
            field=models.PositiveBigIntegerField(),
        ),
    ]
