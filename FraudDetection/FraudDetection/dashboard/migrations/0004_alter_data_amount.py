# Generated by Django 4.0.3 on 2022-05-23 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_data_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
