from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class SimpleViewSet(viewsets.ViewSet, APIView):

    def list(self, request, format=None):
        """
        Получение списка каких то объектов
        :param request:
        :param format:
        :return:
        """
        result = [
            {
                'id': 1,
                'name': 'Some name',
            },
            {
                'id': 2,
                'name': 'Other name',
            },
        ]
        return Response(result)