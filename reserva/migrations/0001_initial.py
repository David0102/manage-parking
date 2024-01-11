# Generated by Django 4.2.7 on 2024-01-09 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cliente", "0002_alter_cliente_cpf"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reserva",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.CharField(
                        choices=[("fixo", "Fixo"), ("rotativo", "Rotativo")],
                        max_length=10,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "horario_entrada",
                    models.DateTimeField(verbose_name="Horário de entrada"),
                ),
                (
                    "horario_saida",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Horário de saída"
                    ),
                ),
                (
                    "valor",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=8,
                        verbose_name="Valor",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("em_andamento", "Em andamento"),
                            ("finalizada", "Finalizada"),
                        ],
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cliente.cliente",
                    ),
                ),
            ],
        ),
    ]
