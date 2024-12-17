from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalogue/", include("catalogue.urls")),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
    path("payment/", include("payment.urls")),
    # These are api urls 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 