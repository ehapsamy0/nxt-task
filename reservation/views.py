from django.shortcuts import render
from rest_framework import generics,permissions,response,status,views

from .permissions import IsCreateOrIsAdmin
from .models import Reservation, ReservationStatus
from .serializers import ReservationDetailsSerializer, ReservationSerializer
import logging

logger = logging.getLogger('myapp.views')


# Create your views here.




class ReservationListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated,IsCreateOrIsAdmin]
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            # Log the start of the request
            logger.info("ReservationListCreateAPIView (List Function): Listing all reservation started")
            rooms = self.filter_queryset(self.get_queryset())
            logger.info("ReservationListCreateAPIView (List Function): Check If Paginations Availabl")
            page = self.paginate_queryset(rooms)
            if page is not None:
                logger.info("ReservationListCreateAPIView (List Function): Paginations to reservation started")
                logger.info("ReservationListCreateAPIView (List Function): Serialize reservation Query With Pagination")
                serializer = self.get_serializer(page, many=True)
                logger.info("ReservationListCreateAPIView (List Function): Listing all reservation completed successfully With Pagination")
                return self.get_paginated_response(serializer.data)
            logger.info("ReservationListCreateAPIView (List Function): Serialize reservation Query")
            serializer = self.get_serializer(rooms, many=True)

            # Log the successful completion of the request
            logger.info("ReservationListCreateAPIView (List Function): Listing all reservation completed successfully")

            return response.Response(serializer.data)
        except Exception as e:
            # Log an error message if an exception occurs
            logger.error(f"ReservationListCreateAPIView (List Function): An error occurred - {str(e)}")
            return response.Response({"error": f"An error occurred {e}."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request, *args, **kwargs):
        logger.info("ReservationListCreateAPIView (Create Function): Start Create Function")
        logger.info(f"Request data: {request.data}")
        req_data = request.data.copy()
        logger.info(f"Modified data: {req_data}")
        req_data['user'] = request.user.id
        serializer = self.get_serializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        logger.info(f"Validated data: {serializer.validated_data}")
        serializer.save()
        logger.info("Reservation created successfully.")
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class ReservationRetrieveAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAdminUser,]
    serializer_class = ReservationDetailsSerializer
    queryset = Reservation.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        ReservationStatus.objects.create(reservation=instance,status=data['status'],user=request.user)
        return response.Response(ReservationDetailsSerializer(instance).data)

