from django.shortcuts import render, redirect
# Create your views here.
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib import messages


# displays the index page
from django.template.loader import render_to_string

from sanpham.models import sanpham, thuonghieu


def index(request):
    sp = sanpham.objects.all()
    th = thuonghieu.objects.all()
    data={'sp':sp,
          'th':th,
    }
    return render(request,'quanlysanpham/index.html',data)


# search view
def search(request):
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            results = sanpham.objects.filter(
                Q(ten__contains=q) |
                Q(masp__contains=q))
            return render(request,'quanlysanpham/results.html', {'results': results},)

def index_th(request,id):
    sp = sanpham.objects.all()
    thuonghieus = thuonghieu.objects.all()
    try:
        th = thuonghieu.objects.get(id=id)
    except thuonghieu.DoesNotExist:
        messages.add_message(request, messages.INFO, 'Có cái gì đó sai sai !')
        return redirect('sanpham:index')

    data={'sp':sp,
          'th':th,
          'thuonghieus':thuonghieus,
    }

    return render(request,'quanlysanpham/index_th.html',data)

def search_thuonghieu(request,id):
    sp = sanpham.objects.all()
    th = thuonghieu.objects.get(id=id)
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            results = th.sanpham_set.filter(
                Q(ten__contains=q) |
                Q(masp__contains=q))
            return render(request,'quanlysanpham/results.html', {'results': results},)