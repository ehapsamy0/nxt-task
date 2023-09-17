from rest_framework import serializers
from account.serializers import UserSerializer
from room.serializers import RoomSerializer
from .models import Reservation,ReservationStatus


class ReservationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservationStatus
        fields = "__all__"



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        extra_kwargs = {
            "total_price": {"required": False},

        }

class ReservationDetailsSerializer(ReservationSerializer):
    room = RoomSerializer()
    changes_history = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer()
    class Meta(ReservationSerializer.Meta):
        pass


    def get_changes_history(self,obj):
        return ReservationStatusSerializer(obj.reservation_history.all(),many=True).data


