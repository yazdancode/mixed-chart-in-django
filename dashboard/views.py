from django.shortcuts import render
from .models import ProductSold, Product
from json import dumps, loads
from django.http import JsonResponse


def index_view(request):
    report = ProductSold().get_report()
    datajson = dumps(report)

    context = {"result": datajson}
    return render(request, "dashboard/index.html", context=context)


def JsonResponseView(request):
    # product =Product.objects.all().values()
    # jsondata = dumps(list(product))


    # # context ={
    # #     "result": jsondata
    # # }
    # # return render(request=request, "dashboard/jsonResponse.html", context=context)

    # # return JsonResponse({"result":jsondata})
    jsondata = '{"id": 1, "name": "digikala"}'
    product = loads(jsondata)
    context = {
        "product": product
    }
    return render(request, "dashboard/jsonResponse.html", context)

