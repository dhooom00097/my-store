"""
URL configuration for neom project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية + الكاتالوج
    path('', include('catalog.urls')),

    # الحسابات (تسجيل / دخول / خروج)
    path('accounts/', include('accounts.urls')),

    # السلة + الطلبات
    path('cart/', include('orders.urls')),
]

# عرض ملفات media أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
