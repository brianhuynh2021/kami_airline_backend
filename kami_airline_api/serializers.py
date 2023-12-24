from rest_framework import serializers

class AirplaneSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    passengers = serializers.IntegerField(required=True)

    def validate(self, data: dict) -> dict:
        """
        Check that the number of passengers is not negative and the id is valid.
        """
        if data['passengers'] < 1:
            raise serializers.ValidationError({"passengers": \
                "Number of passengers cannot be negative."})

        if data['id'] < 1:
            raise serializers.ValidationError({"id": "ID must be a positive number."})

        return data
