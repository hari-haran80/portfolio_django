from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('portfolio_app.urls')),
]+ static(settings.IMAGE_URL, document_root = settings.IMAGE_ROOT)
