from django.contrib import admin

from station.models import Station, Route, TrainType, Train, Crew, Journey


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "latitude", "longitude")
    search_fields = ("name",)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ("id", "source", "destination", "distance")


@admin.register(TrainType)
class TrainTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "cargo_num",
        "places_in_cargo",
        "train_type",
    )


@admin.register(Crew)
class CrewAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "route",
        "train",
        "departure_time",
        "arrival_time",
    )
