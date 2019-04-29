from django.shortcuts import render, redirect
from web import models
# Create your views here.
from web.forms import BookForm


def login(request):

    if request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        user_obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
        if user_obj:
            request.session['pk'] = user_obj.pk
            return redirect('home')
    return render(request, 'login.html')

# 查看
def home(request):

    book_obj = models.Book.objects.all()
    return render(request, 'home.html',{'book_obj':book_obj})
# 添加，
def add(request):

    form_obj = BookForm()
    if request.method == 'POST':
        form_obj = BookForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('home')

    return render(request, 'add.html', {'form_obj': form_obj})





# 编辑
def edit(request,id):
    obj = models.Book.objects.filter(pk=id).first()
    print(obj)
    if request.method == "POST":
        book_obj = BookForm(request.POST, instance=obj)
        print(request.POST.get('name'))
        if book_obj.is_valid():
            print('111')
            book_obj.save()  # 保存修改
            # 跳转到展示页面
            return redirect('home')
    else:
        book_obj = BookForm(instance=obj)

    return render(request, 'edit.html', {"book_obj": book_obj})




def delete(request,id):
    models.Book.objects.filter(pk=id).delete()
    return redirect('home')