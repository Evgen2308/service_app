# Generated by Django 3.2.16 on 2023-09-19 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_plan_plan_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
