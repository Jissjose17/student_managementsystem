from django.urls import path
from clg_app import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('eventpage',views.eventpage,name='eventpage'),
    path('contactpage',views.contactpage,name='contactpage'),
    path('aboutpage',views.aboutpage,name='aboutpage'),
    path('registerfunction',views.registerfunction,name='registerfunction'),
    path('registerpage',views.registerpage,name='registerpage'),
    path('send_registration_email',views.send_registration_email,name='send_registration_email'),
    path('students/', views.show_students, name='show_students'),
    path('deletefunction/<int:data>',views.deletefunction,name='deletefunction'),
    path('editpage/<int:data>',views.editpage,name='editpage'),
    path('editdetails/<int:data>',views.editdetails,name='editdetails'),
    path('profile/<int:data>',views.profile,name='profile'),
]