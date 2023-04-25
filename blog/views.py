from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.

@login_required
def post_list(request):
    """view to return all posts"""
    
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    return render(request, 'blog/post_list.html', {'posts':posts})

@login_required
def post_detail(request, pk):
    """view to return a single post"""
    
    post = get_object_or_404(Post, pk=pk)
    
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    """view to create a new post"""
    
    form = PostForm()
    
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            return redirect('post_detail', pk=post.pk)
        
        else:
            form = PostForm()
            
    return render(request, 'blog/post_edit.html', {'form' : form})

@login_required
def post_edit(request, pk):
    """view to edit a pos"""
    
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = PostForm(request.Post, instance=post)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    """view to return all post drafts"""
    
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    
    return render(request, 'blog/post_draft_list.html', {'posts': posts})