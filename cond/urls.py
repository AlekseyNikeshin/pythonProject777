from  django.urls import path
from . import views

urlpatterns=[
    path("", views.cond_list, name="cond_list"),
    path('cond/<int:pk>/', views.cond_detail, name='cond_detail'),
    path('cond/new/', views.cond_new, name='cond_new'),
    path('cond/<int:pk>/edit/', views.cond_edit, name='cond_edit'),

]