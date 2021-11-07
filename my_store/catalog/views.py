from django.shortcuts import get_object_or_404, render

from .models import Item


def item_list(request):
    items = Item.objects.all()
    # оптимизируем запрос чрез JOIN
    # items = Item.objects.all().select_related('category')
    # отфильтруем
    # items = Item.objects.filter(is_on_main=True).select_related('category')
    # много лишнего
    # items = (
    #     Item.objects
    #     # select_related не обязателен Джанго - умный
    #     .select_related('category')
    #     .filter(is_on_main=True)
    #     .values('name', 'category__name')
    # )
    # items = (
    #     Item.objects
    #     .select_related('category')
    #     .filter(is_on_main=True)
    #     # .prefetch_related('tags')
    #     # values не сработают
    #     # .values('name', 'category__name')
    # )
    context = {
        'items': items,
    }
    return render(request, 'catalog/item_list.html', context)


# Самостоятельная работа
def item_detail(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    context = {
        'item': item,
    }
    return render(request, 'catalog/item_detail.html', context)


# https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#get-object-or-404
# https://github.com/django/django/blob/f83b44075dafa429d59e8755aa47e15577cc49f9/django/db/models/query.py