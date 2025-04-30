from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('auth/', include('apps.authentication.urls')),
    path('vote/', include('apps.voting.urls')),
    path('session/', include('apps.sessions.urls')),
    # path('viz/', include('apps.visualization.urls')),
    # path('control/', include('apps.admincontrols.urls')),
]