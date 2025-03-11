from decimal import Decimal

from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.serializers import *
from basket.basket import Basket
from catalogue.models import *


class ProductClassAPIView(generics.ListCreateAPIView):
    serializer_class = ProductClassSerializer
    queryset = ProductClass.objects.all() 


class ProductCLassDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductClassSerializer
    queryset = ProductClass.objects.all()
    lookup_field = "id"


class CategoryAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCLassDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"


# class ProductCreateAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

#     def get(self, request, category_id=None):
#         if  category_id:
#             products=Product.objects.filter(category_id = category_id)
#         else:
#             products=Product.objects.all()
#         return Response( status=status.HTTP_200_OK)


class ProductCreateAPIView(generics.ListCreateAPIView): 
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, category_id=None):
        if category_id:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = "id"


# @api_view(['POST'])
# def add_to_basket(request):
#     Product.objects.all()
#     return Response(status=status.HTTP_200_OK)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def my_basket(request):
#     basket = Basket(request)
#     l = []
# # {'quantity': 1, 'price': Decimal('125.00'), 'product_name': 'Behari kabab pizza', 'product': <Product: Behari kabab pizza>, 'total_price': Decimal('125.00')}
# # {'quantity': 1, 'price': Decimal('111.00'), 'product_name': 'Chicken Burger', 'product': <Product: Chicken Burger>, 'total_price': Decimal('111.00')}
# # {'quantity': 1, 'price': Decimal('1100.00'), 'product_name': 'Iphone XI', 'product': <Product: Iphone XI>, 'total_price': Decimal('1100.00')}
#     for obj in basket:
#         id = obj['product'].id
#         q = obj['quantity']
#         p = obj['price']
#         n = obj['product_name']

#         l.append({"id": id, "name": n, "quan": q, "proce": p})


#     return Response({"basket": l}, status=status.HTTP_200_OK)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def my_basket(request):
    basket = Basket(request)
    basket_items = []
    for item in basket:
        basket_items.append(
            {
                "product_id": item["product"].id,
                "product_name": item["product_name"],
                "quantity": item["quantity"],
                "price": str(item["price"]),
                "total_price": str(item["total_price"]),
            }
        )
    return Response({"basket": basket_items}, status=status.HTTP_200_OK)


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def add_to_basket(request):
    basket = Basket(request)
    data_from_frontent = list(request.data["products"])
    all_products = Product.objects.filter(name__in=data_from_frontent)
    for obj in all_products:
        basket.add(obj)
    return Response(
        {"message": "Products has been added successfully"}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def remove_from_basket(request):
    basket = Basket(request)
    data_from_frontent = list(request.data["products"])
    all_products = Product.objects.filter(name__in=data_from_frontent)
    for obj in all_products:
        basket.remove(obj.id)
    return Response(
        {"message": "Products has been delete successfully"}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def delete_from_basket(request):
    basket = Basket(request)
    product_id = request.data.get("product_id")

    if not product_id:
        return Response(
            {"message": "Product ID is required."}, status=status.HTTP_400_BAD_REQUEST
        )
    if product_id in basket.basket:
        basket.delete(product_id)
        return Response(
            {
                "message": f"Product with ID {product_id} has been removed from the basket."
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(
            {"message": f"Product with ID {product_id} not found in the basket."},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["POST"])
# @permission_classes([IsAuthenticated])
def checkout(request):
    basket = Basket(request)

    items = []
    total_price = Decimal(0)

    for item in basket:
        items.append(
            {
                "product_name": item["product_name"],
                "quantity": item["quantity"],
                "price": str(item["price"]),
                "total_price": str(item["total_price"]),
            }
        )
        total_price += item["total_price"]

    # Now, you can generate the payment request data, similar to the earlier method
    response_data = {
        "items": items,
        "total_price": str(total_price),
    }

    return Response(response_data, status=200)
