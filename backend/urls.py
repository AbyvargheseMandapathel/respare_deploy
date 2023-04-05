"""respare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('gettopics/',views.topic_api),
    path('gettopic/',views.get_topic),
    path('getchoices/',views.choice_api),
    path('about/',views.about),
    path('register/',views.register),
    path('register/check_uname',views.check_user),
    path('search',views.search,name='search'),
    path('user/<slug:uname>/',views.profile),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
    path('react/',views.react,name="react"), 
    path('topic/<int:pk>/react/',views.react,name="react"), 
    #path('topic/<int:pk>/reactions/',views.reactions),
    path('getreactions/',views.get_reactions),
    path('topic/<int:pk>/reactstatus/',views.is_reacted) ,
    path('topic/<int:pk>/comment/',views.new_comment) ,
    path('topic/<int:pk>/comments/',views.comments) ,
    path('topic/<int:pk>/',views.topic,name='topic'),


]
