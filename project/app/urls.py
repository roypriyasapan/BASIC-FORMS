from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('loindata/',login_data,name='login_data')

]