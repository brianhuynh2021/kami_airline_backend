import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AirplaneSerializer
import math
from drf_spectacular.utils import extend_schema


MAX_AIRPLANES = int(os.getenv('MAX_AIRPLANES', 10))
FUEL_TANK_CAPACITY_MULTIPLIER = int(os.getenv('FUEL_TANK_CAPACITY_MULTIPLIER', 200))
FUEL_CONSUMPTION_MULTIPLIER = float(os.getenv('FUEL_CONSUMPTION_MULTIPLIER', 0.80))
PASSENGER_CONSUMPTION = float(os.getenv('PASSENGER_CONSUMPTION', 0.002))

@extend_schema(
    request=AirplaneSerializer,
    responses={200: AirplaneSerializer, 404: "Not found result"}
)
class AirplaneView(APIView):
    def post(self, request) -> Response:
        if len(request.data) > MAX_AIRPLANES:
            return Response(
                {"message": f"Maximum of {MAX_AIRPLANES} airplanes allowed per request."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AirplaneSerializer(data=request.data, many=True)

        if serializer.is_valid():
            airplanes_info = []

            for airplane_data in serializer.validated_data:
                airplane_id = airplane_data.get('id')
                passengers = airplane_data.get('passengers')

                try:
                    fuel_tank_capacity = FUEL_TANK_CAPACITY_MULTIPLIER * airplane_id
                    fuel_consumption_per_minute = math.log(airplane_id) * FUEL_CONSUMPTION_MULTIPLIER + passengers * PASSENGER_CONSUMPTION
                    max_minutes_able_to_fly = fuel_tank_capacity / fuel_consumption_per_minute

                    airplanes_info.append({
                        "airplane_id": airplane_id,
                        "total_fuel_consumption_per_minute": round(fuel_consumption_per_minute, 6),
                        "max_minutes_able_to_fly": round(max_minutes_able_to_fly, 6)
                    })

                except ValueError as e:
                    return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            return Response(airplanes_info)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)