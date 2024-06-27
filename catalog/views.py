from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def index(request):    #首页视图
    return render(request,'index.html')

# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):   #注册视图
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # 重定向到登录页面
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login(request):   #登录视图
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.is_staff:
                    return redirect('admin')
                else:
                    return render(request,'index.html')
                #return redirect('home')  # 重定向到首页或其他页面
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'index.html')


from .models import Remark
from .forms import RemarkForm  

def list_my_models(request):    #论坛视图
    models = Remark.objects.all()
    return render(request, 'list.html', {'models': models})

@login_required
def add_my_model(request):    #新增贴子视图
    if request.method == 'POST':
        form = RemarkForm(request.POST)
        #request.session['key'] = 'value'
        if form.is_valid():
            input_info = form.save(commit=False)
            input_info.name = request.user
            # 保存信息
            input_info.save()
            models=Remark.objects.all()
            return render(request,'list.html',{'models':models})  # 重定向到列表页面
    else:
        form = RemarkForm()
    return render(request, 'add.html', {'form': form})


@login_required
def user_profile(request):    #个人信息视图
    # 可以添加更多逻辑来获取或更新用户信息
    return render(request, 'user_profile.html', {'user': request.user})


from django.db.models import Q #用于复杂的查询
from .models import Remark

@login_required
def search(request): #ORM（对象关系映射）来构建查询（查询视图）
    keyword = request.GET.get('keyword', '')
    if keyword:
        results = Remark.objects.filter(
            Q(title__icontains=keyword) | Q(content__icontains=keyword)
        )
    else:
        results = Remark.objects.none()
    return render(request, 'search_results.html', {'results': results})

@login_required
def get_mine(request):    #我的贴子视图
    results=request.user.input_infos.all()
    return render(request,'mine_remark.html',{'results':results})

# views.py
from django.shortcuts import get_object_or_404, redirect
from .models import Remark

@login_required
def delete_remark(request):  #删除贴子视图
    post = get_object_or_404(Remark,name=request.user)
    #尝试获取一个Remark对象
    post.delete()
    return render(request,'mine_remark.html')  # 重定向到其他视图，例如列表视图

from .forms import RemarkForm_
@login_required
def change_remark(request):   #修改视图
    remark, created = Remark.objects.get_or_create(name=request.user)
    if request.method == 'POST':
        form = RemarkForm_(request.POST, instance=remark)
        if form.is_valid():
            form.save()
            return render(request,'mine_remark.html',{'results':form}) # 重定向到我的贴子视图
    else:
        form = RemarkForm_(instance=remark)
    return render(request, 'change_remark.html', {'form': form})





















































# from .forms import EmailForm
# def password_reset_form(request):
#     if request.method == 'POST':
#         form = EmailForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             # 这里可以添加发送邮件的逻辑
#             # send_email(email)
#             return render(request, 'password_reset_email.html', {'email': email})
#     else:
#         form = EmailForm()
#     return render(request, 'password_reset_form.html', {'form': form})


# def password_reset_email(request):
#     return render(
#         request,
#         'password_reset_email.html'
#     )

# def password_reset_confirm(request):
#     return render(
#         request,
#         'password_reset_confirm.html'
#     )
# def password_reset_complete(request):
#     return render(
#         request,
#         'password_reset_complete.html'
#     )