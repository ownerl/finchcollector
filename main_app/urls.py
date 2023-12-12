from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finch_show, name='show'),
    path('finches/create/', views.FinchCreate.as_view(), name='create'),
    path('finches/<int:pk>/edit/', views.FinchUpdate.as_view(), name='update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/associate_creator/<int:creator_id>', views.associate_creator, name='associate_creator')
]