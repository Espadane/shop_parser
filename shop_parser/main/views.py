from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages

from .models import User
from .forms import RegisterUserForm, ChangeUserInfoForm

def index(request):
    return render(request, 'main/index.html')

def other_page(request, page):
    """Проверка наличия шаблона"""
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

@login_required
def user_goods(request):
    return render(request, 'main/user_goods.html')

class ShopsLoginView(LoginView):
    model = User
    fields = ['name', 'password']
    template_name = 'main/login.html'
    success_url = reverse_lazy('main:index')
    
class ShopsLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'
    
class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    form_class = ChangeUserInfoForm
    template_name = 'main/profile.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Настройки изменены'
    
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)
    
class ChangeUserPasswordView(PasswordChangeView, LoginRequiredMixin, SuccessMessageMixin):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль изменен'
    
class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')
    
class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'
    
class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')
    
    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)
    
    def logout_user(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
            
        return get_object_or_404(queryset, pk=self.user_id)