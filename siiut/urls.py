from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('career/', include('apps.career.urls')),
    path('accounts/',  include('django.contrib.auth.urls'))
]
