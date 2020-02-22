from django.urls import path
from templateProject import views as tmpviews


urlpatterns = [
    path('urlappview/',tmpviews.tempFirstView),
]