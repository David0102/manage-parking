# Generated by Django 4.2.7 on 2024-01-09 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("vaga", "0001_initial"),
        ("reserva", "0005_alter_reserva_num_vaga"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserva",
            name="num_vaga",
        ),
        migrations.AddField(
            model_name="reserva",
            name="vaga",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="vaga.vaga"
            ),
        ),
    ]
