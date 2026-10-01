from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic import CreateView
from users.forms import UserRegister


class RegisterView(CreateView):
    form_class = UserRegister
    template_name = 'users/register_users.html'
    success_url = reverse_lazy('catalog:product_list')
