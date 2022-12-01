from .views import *
from django.urls import path
urlpatterns =  [
    path('',index , name='index'),
    path('about/', about , name='about'),
    path('contact/',contact, name='contact'),
    path('members/',members_view, name='members'),
    path('Dashboard/',Dashboard, name='Dashboard'),
    path('FAQ/',FAQ, name='FAQ'),
    path('bio/', bio, name='bio'),
    path('next_of_kin/',NEXT_OF_KIN, name='next_of_kin'),
    path('current_acdemic_level/',CURRENT_ACADEMIC_LEVEL, name='current_acdemic_level'),
    path('upload_certificates/',UPLOAD_CERTIFICATES, name='upload_certificates'),
    path('register/',Register,name='register'),
    path('login/',Login_views,name='login'),
    path('logout/',logout_view,name='logout'),
    path('<int:id>/bio_edit/',bio_edit,name='bio_edit')

]