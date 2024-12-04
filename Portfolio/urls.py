from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("portfolio_app.urls")),  # Include app URLs
]

# Serve static files (CSS, JS, etc.) in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve media files (like profile images) in development, only when in DEBUG mode

