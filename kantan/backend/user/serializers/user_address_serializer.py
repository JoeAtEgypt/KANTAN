from rest_framework import serializers


class UserAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    phone = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()
    building = serializers.CharField()
    floor = serializers.CharField()
    apartment = serializers.CharField()
    email = serializers.EmailField()
    is_default = serializers.BooleanField(read_only=True)

