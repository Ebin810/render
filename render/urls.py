from django.contrib import admin
from django.urls import path, include
from myapp.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('myapp.urls')),
    path('', index, name='index'),  # Root URL pointing to the index view
]

urlpatterns += staticfiles_urlpatterns()
