from django.urls import path
from .views import RegisterView, MyAccountView

urlpatterns = [
	path('register/', RegisterView.as_view(), name="register"),
]