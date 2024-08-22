from django.shortcuts import render

from taxi.models import Driver, Car, Manufacturer
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView


def index(request):
    """View function for the home page of the site."""

    context = {
        "num_drivers": Driver.objects.count(),
        "num_cars": Car.objects.count(),
        "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    context_object_name = "manufacturers"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5


class CarListView(generic.ListView):
    model = Car
    queryset = (
        Car.objects.select_related("manufacturer").all().order_by("model"))
    paginate_by = 5


class CarDetailView(DetailView):
    model = Car


class DriverListView(generic.ListView):
    model = Driver
    paginate_by = 5
    queryset = Driver.objects.all().order_by("username")


class DriverDetailView(DetailView):
    model = Driver


def get_queryset(self):
    return Driver.objects.prefetch_related("cars_manufacturer")
