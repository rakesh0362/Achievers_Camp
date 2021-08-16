
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import app_users
import curriculum
import achievers

urlpatterns = [
    path('', include('app_users.urls')),
    path('curriculum/', include('curriculum.urls')),
    path('achievers/', include('achievers.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
