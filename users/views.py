from django.urls import reverse_lazy
from django.views.generic import View

from users.forms import UserRegister


class RegisterView(View):
    form_class = UserRegister
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('catalog:product_list')

#     прописать валидацию и исправить остальное здесь.
