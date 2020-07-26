"""ClassView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from classviewproject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.HelloWorldView.as_view()),
    path('temp/',views.HelloWorldTemplateView.as_view()),
    path('bookList/',views.bookListView.as_view(), name="bookList"),
    path('bookDetail/<int:pk>/',views.bookDetailView.as_view(), name="bookDetail"),
    path('bookCreate/',views.bookCreateView.as_view()),
    path('bookUpdate/<int:pk>/',views.bookUpdateView.as_view()),
    path('bookDelete/<int:pk>/',views.bookDeleteView.as_view()),
]
