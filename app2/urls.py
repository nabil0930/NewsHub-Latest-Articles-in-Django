from django.urls import path
from app2 import views

urlpatterns=[
    path('',views.home1,name='home1'),
    path('addnews',views.addnews,name='addnews'),
    path('delete/<int:pk>',views.delete_,name='delete_'),
    path('update/<int:pk>',views.update,name='update'),
]