from http import HTTPStatus
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from customer.models import Customer

class CustomerListView(APIView):

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="description",
        request_body = CustomerSerializer,
    )
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        customer = serializer.save()
        return Response(data={
            'data': CustomerSerializer(instance=customer).data,
            'success': True
        }, status=HTTPStatus.CREATED)

    def get(self, request):
        return Response({
            'data': [CustomerSerializer(instance=obj).data for obj in Customer.objects.all()],
            'success': True
        }, status=HTTPStatus.OK)


class CustomerDetailView(APIView):
    """
    Retrieve, update or delete a Customer instance.
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        print(f"pk {pk}")
        try:
            obj = get_object_or_404(Customer, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        return Response({
            'data': CustomerSerializer(instance=obj).data,
            'success': True
        }, status=HTTPStatus.OK)

    @swagger_auto_schema(
        operation_description="description",
        request_body = CustomerSerializer,
    )
    def put(self, request, pk):
        try:
            obj = get_object_or_404(Customer, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        serializer = CustomerSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(data={
                **serializer.errors,
                'success': False
            }, status=HTTPStatus.BAD_REQUEST)
        customer = serializer.save()
        return Response(data={
            'data': CustomerSerializer(instance=customer).data,
            'success': True
        }, status=HTTPStatus.OK)

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Customer, pk=pk)
        except Http404:
            return Response(data={
                'message': 'object with given id not found.',
                'success': False
            }, status=HTTPStatus.NOT_FOUND)
        obj.delete()
        return Response(data={
            'message': 'Record Deleted.',
            'success': True
        }, status=HTTPStatus.OK)

