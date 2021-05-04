from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.product_list),
    path("product/<int:idk>/", views.product_detail)
]
