from django.urls import path
from . import views

urlpatterns = [
    path('', views.genupload_bir, name='genupload-bir'),
    path('genupload/', views.genupload_bir, name='genupload-bir'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
]