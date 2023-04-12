from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('print/', views.print, name = "print"),
    path('orderform/', views.orderform, name = "orderform"),
    path('aboutus/', views.aboutus, name = "aboutus"),
    path('acadproject/', views.acadproject, name = "acadproject"),
    path('studymaterial/', views.studymaterial, name = "studymaterial"),
    path('studyguide/', views.studyguide, name = "studyguide"),
    path('homework/', views.homework, name = "homework"),
    path('notebook/', views.notebook, name = "notebook"),
    path('companyproject/', views.companyproject, name = "companyproject"),
    path('businesscard/', views.businesscard, name = "businesscard"),
    path('resume/', views.resume, name = "resume"),
    path('letterhead/', views.letterhead, name = "letterhead"),
    path('billinvoice/', views.billinvoice, name = "billinvoice"),
    path('personaldocs/', views.personaldocs, name = "personaldocs"),
    path('certificate/', views.certificate, name = "certificate"),
    path('presentation/', views.presentation, name = "presentation"),
    path('photoglossy/', views.photoglossy, name = "photoglossy"),
    path('ebook/', views.ebook, name = "ebook"),
]