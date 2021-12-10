
from django.urls import path
from django.conf.urls import url
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login, name='login'),
 
    path('contact',views.contact, name='contact'),
    path('ragister',views.ragister,name='register'),
    path('feedback',views.feedback),
    path('example',views.example),
 
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('update',views.update,name='update'),
    path('question',views.question, name='question'),
    path('edit-profile',views.edit_profile, name='edit-profile'),
    
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path("chat", views.chat, name="chat"),
    
]
 