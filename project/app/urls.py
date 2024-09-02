# from django.contrib import admin
# from django.urls import path
# from .views import *

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('home/',home,name='home'),
#     path('login/',login,name='login'),
    

# ]


from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path("login/",views.login,name='login'),
    path("query/",views.query,name='query'),
    path("delete/<int:pk>",views.delete,name='delete'),
    path("edit/<int:pk>",views.edit,name='edit'),
    path("update/<int:pk>",views.update,name='update'),

]