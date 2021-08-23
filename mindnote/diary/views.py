from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'diary/index.html')

def page_list(request):
    object_list = Page.objects.all()
    paginator = Paginator(object_list, 8)
    curr_page_num = request.GET.get('page')
    if curr_page_num is None:
        curr_page_num = 1
    page = paginator.page(curr_page_num) # Paginator로 부터 하나의 페이지를 가져옵니다.
    return render(request, 'diary/page_list.html', {'page': page}) # 이제는 페이지를 넘겨줍니다.

def page_detail(request, page_id):
    object = Page.objects.get(id=page_id)
    return render(request, 'diary/page_detail.html', {'object': object})

def info(request):
    return render(request, 'diary/info.html')

def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            new_page = form.save()
            return redirect('page-detail', page_id=new_page.id)
    else:
        form = PageForm()
    return render(request, 'diary/page_form.html', {'form': form})

def page_update(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('page-detail', page_id=object.id)
    else:
        form = PageForm(instance=object)
    return render(request, 'diary/page_form.html', {'form': form})

def page_delete(request, page_id):
    object = Page.objects.get(id=page_id)
    if request.method == 'POST':
        object.delete()
        return redirect('page-list')
    else:  # 만약 요청이 GET 방식이라면
        # page_confirm_delete.html을 랜더해서 돌려주도록 합니다.
        # 이때 삭제 확인 페이지에서 글의 제목을 보여줄 수 있도록 object를 함께 넘겨줍니다.
        return render(request, 'diary/page_confirm_delete.html', {'object': object})

