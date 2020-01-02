from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from .models import Balance
from .forms import BalanceForm
from django.urls import reverse_lazy
import logging
from django.conf import settings
import os

class BalanceList(ListView):
  context_object_name = 'balance'
  template_name = 'balance_list.html'
  model = Balance

class DetailBalance(DetailView):
  context_object_name = 'balance'
  template_name = 'balance_detail.html'
  model = Balance

  pagenate_by = 10

def balance_edit(request, balance_id=None):
  if balance_id:
    balance = get_object_or_404(Balance, pk = balance_id)
  else:
    balance = Balance()

  if request.method == 'POST':
    form = BalanceForm(request.POST, instance = balance)

    if form.is_valid():
      balance = form.save()
      return redirect('kakeibo:balance_list')

  else:
    form = BalanceForm(instance=balance)

  return render(request, 'balance_edit.html', dict(form=form, balance_id=balance_id))

def balance_delete(request, balance_id):
  balance = get_object_or_404(Balance, pk = balance_id)

  balance.delete()
  return redirect('kakeibo:balance_list')
