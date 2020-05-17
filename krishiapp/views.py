from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from rest_framework import generics
from rest_framework import permissions
from .models import Crops
from .serializers import CropSerializer

class cropList(generics.ListCreateAPIView):
    queryset = Crops.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self):
    #     queryset = productLine.objects.all()
    #     linename  = self.request.query_params.get('lineName', None)
    #     if linename is not None:
    #         queryset = queryset.filter(lineName = linename)
    #     return queryset

class cropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Crops.objects.all()
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Create your views here.
# def indexView(request):
#     return render(request, "index.html", {})


