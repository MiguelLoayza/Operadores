from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Ops'

urlpatterns = [
    path('', views.index, name='index'),
    path('img/<str:name>', views.operators, name='operators'),
    path('img/<str:name>/data_thresholding', views.image_exponential),
    path('img/<str:name>/data_contrast', views.image_exponential),
    path('img/<str:name>/data_equalization', views.image_exponential),
    path('img/<str:name>/data_exponential', views.image_exponential),
    path('img/<str:name>/data_logarithm', views.image_exponential),
    path('img/<str:name>/data_square', views.image_exponential),
    path('img/<str:name>/data_pow', views.image_exponential),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)