from django.contrib import admin
from django.urls import path, include

urlpatterns = [
<<<<<<< HEAD
    # admin UI if needed:
    # path('admin/', admin.site.urls),

    # Authentication & role selection
    path('', include(('apps.authentication.urls',
                      'authentication'))),

    # session/team & session select
    path('session/', include(('apps.sessions.urls',
                              'sessions'))),

    # voting screens
    path('vote/', include(('apps.voting.urls', 'voting'))),

    # visualization: profile, summaries, progress
    path('viz/', include(('apps.visualization.urls',
                           'visualization'))),

    # admin controls (optional)
    # path('control/', include(('apps.admincontrols.urls',
    #                           'admincontrols'))),
=======
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('vote/', include('apps.voting.urls')),
    path('session/', include('apps.sessions.urls')),
    #path('viz/', include('apps.visualization.urls')),
    #path('control/', include('apps.admincontrols.urls')),
>>>>>>> ibtisam
]
