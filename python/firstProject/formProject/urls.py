from django.urls import path
from formProject import views as frmview

urlpatterns = [
path('register/',frmview.studentRegister),# Application level url 
path('feedback/',frmview.FeedBackView),
]
