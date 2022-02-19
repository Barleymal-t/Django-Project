from django.urls import path
from .views import PostListview
from . import views

urlpatterns = [
    path('', PostListview.as_view(), name ='blog-home'),
    path('about/',views.about, name ='blog-about')
]

# <app>/<model>_<viewtype>.html