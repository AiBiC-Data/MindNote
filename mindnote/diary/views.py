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
        new_page = Page( # 입력된 데이터를 가져와서 Page 데이터 모델을 만들고
            title=request.POST['title'],
            content=request.POST['content'],
            feeling=request.POST['feeling'],
            score=request.POST['score'],
            dt_created=request.POST['dt_created']
        )
        new_page.save() # 데이터베이스에 저장한 후
        return redirect('page-detail', page_id=new_page.id)
    else:  # 만약 요청 방식이 GET이라면
        form = PageForm()  # 새로운 form을 만들고 (빈 폼)
        return render(request, 'diary/page_form.html', {'form': form})
        # 템플릿으로 보내 렌더해서 결과로 돌려줍니다