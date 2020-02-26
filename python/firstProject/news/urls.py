
from django.urls import path
from news import views as nviews


urlpatterns = [
path('jobsurl/',nviews.newsViews),# Application level url 
]



# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# os.path.join(base_dir,'static')