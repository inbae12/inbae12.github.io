from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.mustard, name='mustard'),
    path('/myac', blog.views.myac, name='myac'),
    path('/write', blog.views.write, name='write'),
]
