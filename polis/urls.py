
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('infraestrutura/', include('infraestrutura.urls')),
    path('home/', include('blog.urls')),
    path('api/', include('polis.urls_api')),
    path('usuario/', include('usuario.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
