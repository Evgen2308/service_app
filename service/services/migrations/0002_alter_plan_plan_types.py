# Generated by Django 3.2.16 on 2023-09-14 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_types',
            field=models.CharField(choices=[('full', 'Full'), ('student', 'Student'), ('new_client', 'New_client')], max_length=10),
        ),
    ]
