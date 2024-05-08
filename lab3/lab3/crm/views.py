import json
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Restaurant, MenuItem, Order, OrderItem

@csrf_exempt
@require_http_methods(['GET'])
def restaurants(request):
    restaurant_objects = Restaurant.objects.all()
    return JsonResponse({'restaurants': 'None'})

@csrf_exempt
@require_http_methods(['POST'])
def create_order(request):
#     data = json.loads(request.body)
#     user_id = data.get('user_id')
#     delivery_address = data.get('delivery_address')
#     items = data.get('items', [])
#
#     if not user_id or not delivery_address:
#         return HttpResponseBadRequest('Missing required fields')
#
#     total_price = sum(item['price'] * item['quantity'] for item in items)
#     order = Order.objects.create(user_id=user_id, delivery_address=delivery_address, total_price=total_price)
#
#     for item_data in items:
#         menu_item = MenuItem.objects.get(id=item_data['id'])
#         OrderItem.objects.create(order=order, item=menu_item, quantity=item_data['quantity'])
#
#     return JsonResponse({'order_id': order.id})
    return JsonResponse({'order_id': 'None'})

@csrf_exempt
@require_http_methods(['GET'])
def order_details(request, order_id):
    # order = Order.objects.prefetch_related('items__item').get(id=order_id)
    # order_data = model_to_dict(order)
    # order_data['items'] = [
    #     {
    #         'id': order_item.item.id,
    #         'name': order_item.item.name,
    #         'quantity': order_item.quantity
    #     }
    #     for order_item in order.items.all()
    # ]
    # return JsonResponse(order_data)
    return JsonResponse({'order': 'None'})

@csrf_exempt
@require_http_methods(['GET'])
def menu(request, restaurant_id):
    #menu_items = MenuItem.objects.filter(restaurant_id=restaurant_id)
    return JsonResponse({'menu_items': 'None'})

@csrf_exempt
@require_http_methods(['PUT'])
def update_order(request, order_id):
    # data = json.loads(request.body)
    # delivery_address = data.get('delivery_address')
    # items = data.get('items', [])
    #
    # order = Order.objects.get(id=order_id)
    # order.delivery_address = delivery_address
    # order.total_price = sum(item['price'] * item['quantity'] for item in items)
    # order.save()
    #
    # order.items.all().delete()
    # for item_data in items:
    #     menu_item = MenuItem.objects.get(id=item_data['id'])
    #     OrderItem.objects.create(order=order, item=menu_item, quantity=item_data['quantity'])
    #
    # return JsonResponse({'status': 'ok'})
    return JsonResponse({'order': 'None'})
