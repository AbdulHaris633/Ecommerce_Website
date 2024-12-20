from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("catalogue/", include("catalogue.urls")),
    path("basket/", include("basket.urls")),
    path("checkout/", include("checkout.urls")),
    path("payment/", include("payment.urls")),
    # These are api urls
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/password/change/", include("dj_rest_auth.urls")),
    path("api/productclass/", ProductClassAPIView.as_view()),
    path("api/productclass/detail/<uuid:id>/", ProductCLassDetailAPIView.as_view()),
    path("api/categories/", CategoryAPIView.as_view()),
    path("api/categories/detail/<uuid:id>/", CategoryCLassDetailAPIView.as_view()),
    path("api/products/", ProductCreateAPIView.as_view()),
    path("api/products/<uuid:category_id>/", ProductCreateAPIView.as_view()),
    path("api/product/detail/<uuid:id>/", ProductDetailAPIView.as_view()),
    path("api/basket/", my_basket),
    path("api/add_to_basket/", add_to_basket),
    path("api/remove_from_basket/", remove_from_basket),
    path("api/delete_from_basket/", delete_from_basket),
    path("api/checkout/", checkout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
