# Generated by Django 5.0.2 on 2024-03-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0002_alter_producto_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(default='Sin categoría', max_length=100),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0, max_length=7),
        ),
    ]