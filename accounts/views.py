from django.contrib.auth.forms import  UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from base.models import Post

# New Users
'''
john - john@pass

'''

# Create your views here.
class RegisterView(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'register.html'