from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group


def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() #появляется новый пользователь,
            category = request.POST['account_type']
            if category == 'author': #если выбрали категорю автора, отправляем на проверку
                group = Group.objects.get(name='Actions Required')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='Reader')
                user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
 #           account = Account.objects.create(user=user,nickname=user.username)
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,f'{username} был зарегистрирован!')

            return redirect('blog-home')

    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'users/register.html',context)




# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

#ограничение доступа к профилям для незарегистрированных пользователей
@login_required
def profile(request):
    return render(request, 'users/profile.html')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# def registration(request):
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save() #появляется новый пользователь
#             category = request.POST['account_type']
#             if category == 'author':
#                 group = Group.objects.get(name='Actions Required')
#                 user.groups.add(group)
#     #         else:
    #             group = Group.objects.get(name='Reader')
    #             user.groups.add(group)
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         account = Account.objects.create(user=user,nickname=user.username)
    #         user = authenticate(username=username,password=password)
    #         login(request,user)
    #         messages.success(request,f'{username} был зарегистрирован!')
    #
    #         return redirect('blog-home')
    # else:
    #     form = UserCreationForm()
    # context = {'form':form}
    # return render(request,'users/register.html',context)