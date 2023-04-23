from . import views
from django.urls import path
app_name='googleapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('marriage',views.marriage,name='marriage'),
    path('news',views.news,name='news')
]