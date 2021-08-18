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
    if request.method == 'POST': # 만약 요청 방식이 POST라면
        form = PageForm(request.POST)  # 입력된 데이터와 폼을 합쳐서 바인딩 폼을 만듭니다.
        new_page = form.save()  # 데이터 저장 및 생성된 데이터 모델 반환
        return redirect('page-detail', page_id=new_page.id)
    else:  # 만약 요청 방식이 GET이라면
        form = PageForm()  # 새로운 form을 만들고 (빈 폼)
        return render(request, 'diary/page_form.html', {'form': form})
        # 템플릿으로 보내 렌더해서 결과로 돌려줍니다