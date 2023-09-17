from .serializers import ReservationSerializer
from .models import Reservation


class ReservationService:


    @staticmethod
    def create_reservation(user, data):
        try:
            data['user'] = user.id
            serializer = ReservationSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            raise Exception(f"Error creating reservation: {str(e)}")