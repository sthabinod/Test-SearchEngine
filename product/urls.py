
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('shop-details/<id>', views.shop_details, name="details"),
    path('all-goods', views.all_goods, name="all-goods"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
