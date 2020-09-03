from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def declarations_list(request):
    return render(request, 'declarations/list.html')


@login_required
def declaration_detail(request):
    return render(request, 'declarations/detail.html')
