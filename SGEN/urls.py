from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views.LoginView import Login_View


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login_View, name='login'),
    path('', include('accounts.urls.urls')),
    path('', include('loans.urls.urls')),
] + static (settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
