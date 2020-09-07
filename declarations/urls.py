from django.urls import path

from . import views

urlpatterns = [
    path('', views.declarations_list, name='declarations_list'),
    path('detail/262/', views.declaration_detail, name='declaration_detail'),
    path('export/pdf/mock/', views.declaration_pdf_gen, name='declaration_pdf_gen'),
]
