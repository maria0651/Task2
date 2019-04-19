from django.urls import path
from thirdapp import views

urlpatterns = [
    path('third',views.random2,name='random2')


]