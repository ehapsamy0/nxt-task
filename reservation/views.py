from django.shortcuts import render
from rest_framework import generics,permissions,response,status,views

from .services import ReservationService

from .permissions import IsCreateOrIsAdmin
from .models import Reservation, ReservationStatus
from .serializers import ReservationDetailsSerializer, ReservationSerializer
import logging

logger = logging.getLogger('myapp.views')


# Create your views here.



from rest_framework import generics

class ReservationListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsCreateOrIsAdmin]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def create(self, request, *args, **kwargs):
        logger.info("ReservationListCreateAPIView (Create Function): Start Create Function")
        req_data = request.data.copy()
        try:
            ReservationService.create_reservation(request.user, req_data)
            logger.info("Reservation created successfully.")
            return response.Response({"message": "Reservation created successfully."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"ReservationListCreateAPIView (Create Function): An error occurred - {str(e)}")
            return response.Response({"error": f"An error occurred: {str(e)}."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ReservationRetrieveAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = ReservationDetailsSerializer
    queryset = Reservation.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info("ReservationRetrieveAPIView (Update Function): Start update Function to change reservation status")
        data = request.data
        if "status" in data:
            ReservationStatus.objects.create(reservation=instance,status=data['status'],user=request.user)
            return response.Response(ReservationDetailsSerializer(instance).data,status=status.HTTP_200_OK)
        logger.error("ReservationRetrieveAPIView (Update Function): error ther is no status in request data")
        return response.Response(
            {
                "message":"ther is no status in request data"
            },
            status=status.HTTP_400_BAD_REQUEST
        )
