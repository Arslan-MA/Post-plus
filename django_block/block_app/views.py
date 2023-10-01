from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from block_app.models import Post
from block_app.forms import PostModelForm


def main_page(request):
    context = {'posts': Post.objects.all()}

    return render(request, 'block_app/mainPage.html', context)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'forms': form}

    return render(request, 'block_app/register.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,
                            username=username,
                            password=password)
        if user:
            login(request, user)
            return redirect('home')
    context = {'form': AuthenticationForm()}
    return render(request, 'block_app/login.html', context)


class PasswordChangePage(PasswordChangeView):
    template_name = 'block_app/edit_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')


class PasswordResetPage(PasswordResetView):
    template_name = 'block_app/reset_password.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('home')


def logout_page(request):
    logout(request)
    return redirect('home')


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostModelForm()

    context = {'forms': form}

    return render(request, 'block_app/addPost.html', context)


class EditPostPage(UpdateView):
    model = Post
    template_name = 'block_app/editPost.html'
    form_class = PostModelForm
    success_url = reverse_lazy('home')


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')
