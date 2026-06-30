from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from station.models import (
    Station,
    Route,
    TrainType,
    Train,
    Crew,
    Journey,
    Order,
)
from station.permissions import IsAdminOrReadOnly
from station.serializers import (
    StationSerializer,
    RouteSerializer,
    RouteListSerializer,
    TrainTypeSerializer,
    TrainSerializer,
    TrainListSerializer,
    CrewSerializer,
    JourneySerializer,
    JourneyListSerializer,
    JourneyDetailSerializer,
    OrderSerializer,
    OrderDetailSerializer,
)


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.select_related(
        "source",
        "destination",
    )
    serializer_class = RouteSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("source__name", "destination__name")

    def get_serializer_class(self):
        if self.action == "list":
            return RouteListSerializer

        return RouteSerializer


class TrainTypeViewSet(viewsets.ModelViewSet):
    queryset = TrainType.objects.all()
    serializer_class = TrainTypeSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TrainViewSet(viewsets.ModelViewSet):
    queryset = Train.objects.select_related(
        "train_type",
    )
    serializer_class = TrainSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "train_type__name")

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer

        return TrainSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("first_name", "last_name")


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = (
        Journey.objects
        .select_related(
            "route",
            "train",
        )
        .prefetch_related("crew")
    )
    serializer_class = JourneySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "route__source__name",
        "route__destination__name",
        "train__name",
    )

    def get_serializer_class(self):
        if self.action == "list":
            return JourneyListSerializer

        if self.action == "retrieve":
            return JourneyDetailSerializer

        return JourneySerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return (
            Order.objects.filter(user=self.request.user)
            .select_related("user")
            .prefetch_related(
                "tickets",
                "tickets__journey",
            )
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer

        return OrderSerializer