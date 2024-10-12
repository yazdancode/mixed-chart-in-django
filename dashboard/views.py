from django.shortcuts import render
from .models import ProductSold
from json import dumps


def index_view(request):
    report = ProductSold().get_report()
    datajson = dumps(report)

    context = {"result": datajson}
    return render(request, "dashboard/index.html", context=context)
