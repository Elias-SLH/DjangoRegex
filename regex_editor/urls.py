from django.urls import path

from . import views


app_name = 'regex_editor'
urlpatterns = [
    path('', views.RegexFormView.as_view(), name='index'),
]
