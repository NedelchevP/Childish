from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action

from onlinestore.models import Product, Orders
from onlinestore.pagination import StandardResultsSetPagination
from onlinestore.serializers import ProductSerializer, OrdersSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    # filterset_class = BrandFilter
    ordering_fields = ['title', 'price']
    pagination_class = StandardResultsSetPagination

    # def create(self, request, *args, **kwargs):
    #     """Override CREATE"""
    #     return super(ProductViewSet, self).create(request, *args, **kwargs)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     """Override RETRIEVE"""
    #     return super(ProductViewSet, self).retrieve(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     """Override UPDATE"""
    #     return super(ProductViewSet, self).update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     """Override DESTROY"""
    #     return super(ProductViewSet, self).destroy(request, *args, **kwargs)
    #
    # def list(self, request, *args, **kwargs):
    #     """Override LIST and adds django-filter functionality ??"""
    #     return super(ProductViewSet, self).list(request, *args, **kwargs)

class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    # filterset_class = BrandFilter
    ordering_fields = ['date']
    pagination_class = StandardResultsSetPagination

    # def create(self, request, *args, **kwargs):
    #     """Override CREATE"""
    #     return super(OrdersViewSet, self).create(request, *args, **kwargs)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     """Override RETRIEVE"""
    #     return super(OrdersViewSet, self).retrieve(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     """Override UPDATE"""
    #     return super(OrdersViewSet, self).update(request, *args, **kwargs)
    #
    # def destroy(self, request, *args, **kwargs):
    #     """Override DESTROY"""
    #     return super(OrdersViewSet, self).destroy(request, *args, **kwargs)
    #
    # def list(self, request, *args, **kwargs):
    #     """Override LIST and adds django-filter functionality ??"""
    #     return super(OrdersViewSet, self).list(request, *args, **kwargs)

    """
    @action(detail=True, methods=['post'])
    def remove_user(self, request, pk):
        brand_id = pk
        user_id = request.data.get('user_id') if 'user_id' in request.data else None
        if not (brand_id and brand_id.isnumeric()) or not (user_id and user_id.isnumeric()):
            return Response({"error": 'brand_id(int) AND user_id(int) are required!'},
                            status=status.HTTP_400_BAD_REQUEST)
        brand = Brand.objects.get(pk=brand_id)
        user = User.objects.get(pk=user_id)
        brand.users.remove(user)
        return Response({"message": f"removed user {user.email}({user.id}) from the brand {brand.name}({brand.id})!"})

    @action(detail=False, methods=['get'])
    def get_brand_categories(self, request):
        return Response(dict((x.id, x.name) for x in BrandCategory.objects.all()))

    """