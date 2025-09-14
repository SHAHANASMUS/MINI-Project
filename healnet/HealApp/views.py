from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout,get_user_model
from .forms import CustomUserCreationForm,BlogForm
from django.contrib.auth.decorators import login_required
from .models import Blog

User = get_user_model()
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.role == "general":
                return redirect('general_home')  # or wherever you want
            else:
                return redirect('patient_home')  # or wherever you want
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login or home
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def home(request):
    return render(request, 'home.html')
def patient_home(request):
    all_users = User.objects.exclude(id=request.user.id)
    return render(request, "patient_home.html", {"user": request.user, "all_users": all_users })
def general_home(request):
    all_users = User.objects.exclude(id=request.user.id)
    return render(request, "general_home.html", {"user": request.user, "all_users": all_users })
# Create Blog
@login_required
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # assign logged-in user
            blog.save()
            return redirect("view_blog")
    else:
        form = BlogForm()
    return render(request, "create_blog.html", {"form": form})

# View all blogs
def view_blogs(request):
    blogs = Blog.objects.all().order_by("-created_at")
    return render(request, "view_blogs.html", {"blogs": blogs})


def search_blogs(request):
    return render(request, 'search_blogs.html')

def messages(request):
    return render(request, 'messages.html')
def connection_requests(request):
    return render(request, 'connection_requests.html')
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('view_blogs')
    return render(request, 'delete_blog.html', {'blog': blog})
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id, author=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

