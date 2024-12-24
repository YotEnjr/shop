from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import *
from .models import *
from .utils import *

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
# Create your views here.


@login_required
def userpage(request):
    return render(request, 'userpage/userpage.html', {})


@login_required
def basket(request):
    return render(request, 'userpage/basket.html', {})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('homepage:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))
