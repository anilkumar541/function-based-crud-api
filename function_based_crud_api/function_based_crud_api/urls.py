
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.products, name='products'),
    path("<int:pk>/", views.products_detail, name='products_detail')

]
