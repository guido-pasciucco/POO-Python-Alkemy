# Generated by Django 5.0.2 on 2024-03-13 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
