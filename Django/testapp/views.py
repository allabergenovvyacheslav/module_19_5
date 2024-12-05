from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post, Test_Table, Table_New

# Create your views here.


def table(request):
    table_new = Table_New.objects.all()
    return render(request, 'table.html', {'table_new': table_new})


def test(request):
    test_table = Test_Table.objects.all()
    return render(request, 'test.html', {'test_table': test_table})


def index(request):
    posts = Post.objects.all().order_by('created_at')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})