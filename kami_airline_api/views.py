from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AirplaneSerializer
from .utils import airplane_exists
import math

class AirplaneView(APIView):
    def post(self, request):
        serializer = AirplaneSerializer(data=request.data)

        if serializer.is_valid():
            airplane_id = serializer.validated_data.get('id')
            if not airplane_exists(airplane_id):
                return Response({"message": "Airplane does not exist. \
                                    Valid airplane IDs range from 1 to 10"},
                                status=status.HTTP_400_BAD_REQUEST)
            passengers = serializer.validated_data.get('passengers')

            try:
                fuel_tank_capacity = 200 * airplane_id
                fuel_consumption_per_minute = math.log(airplane_id) * 0.80 + passengers * 0.002
                max_minutes_able_to_fly = fuel_tank_capacity / fuel_consumption_per_minute

                return Response({
                    "total_fuel_consumption_per_minute": fuel_consumption_per_minute,
                    "max_minutes_able_to_fly": max_minutes_able_to_fly
                })
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
