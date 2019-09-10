from django.urls import path
from . import views

app_name ='posts'

urlpatterns = [
    path('blog/', views.post_list,name='post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]