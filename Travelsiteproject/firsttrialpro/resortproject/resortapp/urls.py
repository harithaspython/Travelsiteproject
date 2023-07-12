from . import views
from django.urls import path
urlpatterns = [

    path('', views.demo, name="demo")      # our main page-->calculate.html
    # path('about/', views.about, name="about"),
    # path('add/', views.addition, name="addition")
]
