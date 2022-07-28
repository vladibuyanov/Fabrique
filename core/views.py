from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .serializers import MailingListSerializer, ClientSerializer
from .models import MailingList, Client
from .statistic import full_statistic, detailed_statistics


class MailingListViews(CreateModelMixin,
                       UpdateModelMixin,
                       DestroyModelMixin,
                       GenericViewSet):
    queryset = MailingList.objects.all()
    serializer_class = MailingListSerializer


class ClientViews(CreateModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class Mailing_list_statistic(APIView):
    @staticmethod
    def get(request, pk=0):
        if not pk:
            return Response(full_statistic())
        else:
            return Response(detailed_statistics(pk))
