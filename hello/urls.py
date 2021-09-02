from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "perry ice cream"
admin.site.site_title = "perry ice cream Portal"
admin.site.index_title = "Welcome to perry ice cream "

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include ('home.urls')),
    path("about",include ('home.urls')),
    path("accounts/",include ('accounts.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
   

