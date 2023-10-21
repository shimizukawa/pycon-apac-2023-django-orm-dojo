from django.shortcuts import render
from .models import Staff


def staff_list(request):
    queryset = Staff.objects.order_by("last_login").only("pk", "name")
    return render(request, "index.html", context={"staffs": queryset})


def staff_detail(request, id):
    pass
