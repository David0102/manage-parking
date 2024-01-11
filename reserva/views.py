from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from reserva.models import Reserva
from vaga.models import Vaga
from cliente.models import Cliente
from django.contrib import messages
from datetime import datetime
import pytz
from django.contrib.auth.decorators import login_required

class ReservaListView(LoginRequiredMixin ,ListView):
    model = Reserva
    context_object_name = 'reservas'
    template_name = 'reserva/reservas.html'

    def get_queryset(self):
        return Reserva.objects.all().order_by('-horario_entrada')

@login_required
def cadastrar_reserva(request):
    if request.method == "GET":
        vagas_dispo = Vaga.objects.filter(disponivel=True)
        clientes = Cliente.objects.all()
        return render(request, 'reserva/cadastrar_reserva.html', {'vagas_dispo': vagas_dispo, 'clientes': clientes})
    
    if request.method == "POST":
        cliente_id = request.POST.get('cliente_id')
        num_vaga = request.POST.get('num_vaga')
        entrada = request.POST.get('entrada')
        saida = request.POST.get('saida')

        entrada_datetime = datetime.strptime(entrada, '%Y-%m-%dT%H:%M')

        cliente = Cliente.objects.get(id=cliente_id)
        vaga = Vaga.objects.get(numero=num_vaga)

        if saida:
            saida_datetime = datetime.strptime(saida, '%Y-%m-%dT%H:%M')
            reserva = Reserva(
                cliente = cliente,
                horario_entrada = entrada_datetime,
                horario_saida = saida_datetime,
                vaga = vaga
            )
            reserva.save()
            reserva.calcula_valor()

            vaga.cliente = cliente
            vaga.disponivel = False
            vaga.save()

            messages.success(request, 'Reserva cadastrada com sucesso!')
            return redirect('reservas')
        else:
            reserva = Reserva(
                cliente = cliente,
                horario_entrada = entrada_datetime,
                horario_saida = None,
                vaga = vaga
            )
            reserva.save()

            vaga.cliente = cliente
            vaga.disponivel = False
            vaga.save()

            messages.success(request, 'Reserva cadastrada com sucesso!')
            return redirect('reservas')

@login_required
def finalizar_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    vaga = Vaga.objects.get(numero=reserva.vaga.numero)

    if reserva.horario_saida:
        reserva.status = 'finalizada'
        reserva.save()
        vaga.cliente = None
        vaga.disponivel = True
        vaga.save()
        return redirect('reservas')
    
    fuso_local = pytz.timezone('America/Sao_Paulo')
    data_atual = datetime.now(fuso_local)
    reserva.horario_saida = data_atual
    reserva.status = 'finalizada'
    reserva.save()
    reserva.calcula_valor()
    vaga.cliente = None
    vaga.disponivel = True
    vaga.save()
    return redirect('reservas')

@login_required
def confirm_delete(request, id):
    reserva = Reserva.objects.get(id=id)
    return render(request, 'reserva/deletar_reserva.html', {'reserva':reserva})

def deletar_reserva(request):
    reserva_id = request.POST.get('reserva_id')
    reserva = Reserva.objects.get(id=reserva_id)
    vaga = Vaga.objects.get(numero=reserva.vaga.numero)

    if reserva.status == 'em_andamento':
        reserva.delete()
        vaga.cliente = None
        vaga.disponivel = True
        vaga.save()
        messages.success(request, 'Reserva excluída com sucesso!')
        return redirect('reservas')
    
    reserva.delete()
    messages.success(request, 'Reserva excluída com sucesso!')
    return redirect('reservas')