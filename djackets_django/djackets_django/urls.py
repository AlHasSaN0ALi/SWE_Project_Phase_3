from django.contrib import admin
from django.urls import path , include
from django.urls import path, include
from product import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),

     path('', views.LatestProductsList.as_view(), name='home'),  
    path('latest-products/', views.LatestProductsList.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('latest-products/', views.LatestProductsList.as_view()),
# ]