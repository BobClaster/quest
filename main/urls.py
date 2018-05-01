from django.urls import path
from .views import login_page, is_logged

urlpatterns = [
    path('', login_page, name='login-page'),
    path('logged/', is_logged, name='is-logged'),
]
