from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.index, name='index'),  # Dodanie ścieżki do strony głównej
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('employee_create/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('generate_contract/<int:pk>/', views.generate_contract, name='generate_contract'),
    path('delete_contract/<int:pk>/', views.delete_contract, name='delete_contract'),
    path('select_template/<int:pk>/', views.select_template, name='select_template'),
    path('fetch_placeholders/', views.fetch_placeholders, name='fetch_placeholders'),
    path('get_employee_data/', views.get_employee_data, name='get_employee_data'),


]
