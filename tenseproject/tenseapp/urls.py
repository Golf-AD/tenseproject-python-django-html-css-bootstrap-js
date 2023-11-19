from django.urls import path
from tenseapp import views
from .views import HomeView



urlpatterns = [
    path('',views.base),
    path('index',views.index),
    path('present',views.present),
    path('past',views.past),
    path('future',views.future),
    path('about',views.about),
    #path('', HomeView.as_view(), name='index'),
]
