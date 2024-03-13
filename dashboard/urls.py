from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('banner-list/', views.list_banner, name='banner-list'),
    path('banner-create/', views.create_banner, name='banner-create'),
    path('banner-detail/<int:id>/', views.banner_detail, name='banner_detail'),
    path('banner-edit/<int:id>/', views.banner_edit, name='banner_edit'),
    path('banner-delete/<int:id>/', views.banner_delete, name='banner_delete'),

    path('server-create/', views.create_service, name='server-create'),
    path('server-list/', views.list_service, name='server-list'),
    path('service-detail/<int:id>/', views.service_detail, name='service_detail'),
    path('service-edit/<int:id>/', views.service_edit, name='service_edit'),
    path('service-delete/<int:id>/', views.service_delete, name='service_delete'),

    path('aboutus-create/', views.create_aboutus, name='aboutus-create'),
    path('aboutus-list/', views.list_aboutus, name='aboutus-list'),
    path('about-edit/<int:id>/', views.aboutus_edit, name='aboutus_edit'),
    path('about-delete/<int:id>/', views.aboutus_delete, name='aboutus_delete'),
    path('aboutus-detail/<int:id>/', views.aboutus_detail, name='aboutus_detail'),
    
    path('price-create/', views.create_price , name='price-create'),
    path('price-list/', views.list_price, name='price-list'),
    path('price-edit/<int:id>/', views.price_edit, name='price_edit'),
    path('price-delete/<int:id>/', views.price_delete, name='price_delete'),
    path('price-detail/<int:id>/', views.price_detail, name='price_detail'),

    path('contact-detail/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contact-edit/<int:id>/', views.contact_edit, name='contact_edit'),
    path('contact-list/', views.contact_list, name='contact_list'),
    
    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
    
    path('q', views.query, name='query')
]