# Generated by Django 4.2.7 on 2025-06-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_expenses_options_alter_incomes_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incomes',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
