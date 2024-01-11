# Generated by Django 4.2.7 on 2024-01-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reserva", "0007_alter_reserva_vaga"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reserva",
            name="tipo",
            field=models.CharField(
                choices=[("fixa", "Fixa"), ("rotativa", "Rotativa")],
                max_length=10,
                verbose_name="Tipo",
            ),
        ),
    ]