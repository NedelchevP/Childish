from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from onlinestore.models import Product, Orders
from onlinestore.pagination import StandardResultsSetPagination
from onlinestore.serializers import ProductSerializer, OrdersSerializer, ApiStatsSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []
    ordering_fields = ['title', 'price']
    pagination_class = StandardResultsSetPagination


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = []
    ordering_fields = ['date']
    pagination_class = StandardResultsSetPagination


class ApiStats(GenericViewSet):
    serializer_class = ApiStatsSerializer
    queryset = Orders.objects.all()
    permission_classes = []

    @action(detail=False, methods=['post'])
    def stats(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            from django.db.models import Count, Sum, CharField, Value
            from django.db.models.functions import ExtractMonth, ExtractYear, Concat

            month_queryset = self.queryset.values('id', 'date', 'products').annotate(month_num=ExtractMonth('date'),
                                                                                     year_num=ExtractYear('date'),
                                                                                     month=Concat('year_num',
                                                                                                  Value('-'),
                                                                                                  'month_num',
                                                                                                  output_field=CharField()))

            final_queryset = None
            if serializer.validated_data['metric'] == 'price':
                final_queryset = month_queryset.values('month').annotate(value=Sum('products__price'))
            elif serializer.validated_data['metric'] == 'count':
                final_queryset = month_queryset.values('month').annotate(value=Count('products'))
            return Response(final_queryset)
