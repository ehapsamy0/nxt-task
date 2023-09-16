from django.shortcuts import render
from rest_framework import generics,permissions,response,status
from .models import Room
from .serializers import RoomSerializer
import logging

logger = logging.getLogger('myapp.views')


# Create your views here.


class RoomListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            # Log the start of the request
            logger.info("RoomListAPIView: Listing all rooms started")
            rooms = self.filter_queryset(self.get_queryset())
            logger.info("RoomListAPIView: Check If Paginations Availabl")
            page = self.paginate_queryset(rooms)
            if page is not None:
                logger.info("RoomListAPIView: Paginations to rooms started")
                logger.info("RoomListAPIView: Serialize Rooms Query With Pagination")
                serializer = self.get_serializer(page, many=True)
                logger.info("RoomListAPIView: Listing all rooms completed successfully With Pagination")
                return self.get_paginated_response(serializer.data)
            logger.info("RoomListAPIView: Serialize Rooms Query")
            serializer = self.get_serializer(rooms, many=True)

            # Log the successful completion of the request
            logger.info("RoomListAPIView: Listing all rooms completed successfully")

            return response.Response(serializer.data)
        except Exception as e:
            # Log an error message if an exception occurs
            logger.error(f"RoomListAPIView: An error occurred - {str(e)}")
            return response.Response({"error": "An error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



