#from django.conf.urls import url
from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [ path('', views.course_list, name='course_list'),
                path('<int:course_pk>/<int:step_pk>', views.step_detail, name='step'),
                path('<int:pk>/', views.course_detail, name='detail'),

]
