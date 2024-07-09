from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import settings

from cars.views import ShowCar, NewCar, CarDetail, CarUpdate, CarDelete
from account.views import login_auth, logout_auth, Register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name='register'),
    path('login/', login_auth, name='login'),
    path('logout/', logout_auth, name='logout'),
    path('cars/', ShowCar.as_view(), name='cars_list'),
    path('new_car/', NewCar.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetail.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdate.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDelete.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
