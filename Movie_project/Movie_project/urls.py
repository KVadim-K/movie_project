from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView  # Добавлено перенаправление RedirectView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('films/', include('films.urls')),  # Добавлено перенаправление films/
                  path('admin_pan/', include('admin_pan.urls')),
                  path('', RedirectView.as_view(url='/admin_pan/', permanent=True)),  # Добавлено перенаправление
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
