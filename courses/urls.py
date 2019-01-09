#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [ path('', views.course_list),
                path('<int:pk>/', views.course_detail),
]
