from django.urls import path
from templateProject import views 


urlpatterns = [
    path('urlappview/',views.tempFirstView),
    path('profile/',views.profileView),
]