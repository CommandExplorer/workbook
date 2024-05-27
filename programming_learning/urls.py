from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('workbook.urls')),
    path('accounts/', include('accounts.urls')),
    path('practice_work/', include('practice_work.urls')),
]