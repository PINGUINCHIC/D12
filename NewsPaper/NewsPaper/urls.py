from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('newapp.urls')),
    path('sign/', include('sign.urls')),
    path('protect/', include('protect.urls')),
    path('accounts/', include('allauth.urls')),
]