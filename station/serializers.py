from rest_framework import serializers

from station.models import (
    Station,
    Route,
    TrainType,
    Train,
    Crew,
    Journey,
    Order,
    Ticket,
)


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ("id", "name", "latitude", "longitude")


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ("id", "source", "destination", "distance")


class RouteListSerializer(RouteSerializer):
    source = serializers.CharField(source="source.name", read_only=True)
    destination = serializers.CharField(
        source="destination.name",
        read_only=True,
    )


class TrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainType
        fields = ("id", "name")


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "cargo_num",
            "places_in_cargo",
            "train_type",
        )


class TrainListSerializer(TrainSerializer):
    train_type = serializers.CharField(
        source="train_type.name",
        read_only=True,
    )


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name")


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = (
            "id",
            "route",
            "train",
            "crew",
            "departure_time",
            "arrival_time",
        )


class JourneyListSerializer(JourneySerializer):
    route = RouteListSerializer(read_only=True)
    train = TrainListSerializer(read_only=True)


class JourneyDetailSerializer(JourneySerializer):
    route = RouteSerializer(read_only=True)
    train = TrainSerializer(read_only=True)
    crew = CrewSerializer(many=True, read_only=True)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "cargo", "seat", "journey")


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ("id", "created_at", "tickets")


class OrderDetailSerializer(OrderSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
