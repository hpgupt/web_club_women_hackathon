from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^todolist/', include("todolist.urls" , namespace="todolist")),
    
    url(r'^admin/', admin.site.urls),
]