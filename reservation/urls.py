from django.urls import path
from .views import ReservationListCreateAPIView,ReservationRetrieveAPIView

urlpatterns = [
    path('', ReservationListCreateAPIView.as_view(), name='reservations'),
    path('<int:pk>/', ReservationRetrieveAPIView.as_view(), name='reservations'),
    
    
]
