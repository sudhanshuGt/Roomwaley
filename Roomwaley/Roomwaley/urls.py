
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import mainpage, about



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainpage),
    path('about/', about, name='about'),
    path('profile/',  include('myprofile.urls')),
    path('home/', include('home.urls')),
    path('chat/', include('chat.urls')),
    path('login/', include('login_signup.urls')),
    path('post/', include('postrooms.urls'))
]
