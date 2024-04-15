from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from .models import Menu, Booking

from .serializers import (
    MenuSerializer,
    BookingSerializer,
    UserSerializer,
)
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import permission_classes
# Create your views here.
def index(request):
    return render(request, "index.html", {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer