from django.urls import path
from secondapp import views


urlpatterns = [
    path('second',views.random,name='random'),

]