# Generated by Django 4.2.7 on 2024-01-09 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cliente", "0002_alter_cliente_cpf"),
        ("vaga", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vaga",
            name="status",
        ),
        migrations.AddField(
            model_name="vaga",
            name="disponivel",
            field=models.BooleanField(default=True, verbose_name="Disponível"),
        ),
        migrations.AlterField(
            model_name="vaga",
            name="cliente",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="cliente.cliente",
            ),
        ),
    ]