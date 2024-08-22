from django.urls import path
from .views import PessoaFormView


urlpatterns = [
    path('pessoa/', PessoaFormView.as_view(), name='pessoa'),
]
