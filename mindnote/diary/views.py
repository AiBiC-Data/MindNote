from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm

# Create your views here.
def page_list(request):
    object_list = Page.objects.all()  # 데이터 조회
    return render(request, 'diary/page_list.html', {'object_list': object_list})

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