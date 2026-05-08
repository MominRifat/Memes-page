from django.shortcuts import redirect, render

from .form import memeform

from .models import Meme

# Create your views here.
def home(request):
    memes = Meme.objects.all()
    return render(request, 'home.html', {'memes': memes})

def post(request):
    if request.method == 'POST':
        form = memeform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = memeform(request.FILES)

    return render(request, 'post.html', {'form': form})


def view(request):
    memes = Meme.objects.all()
    return render(request, 'view.html', {'memes': memes})

def update(request,id):
    memes = Meme.objects.get(pk=id)
    if request.method == 'POST':
        form = memeform(request.POST, request.FILES,instance=memes)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form = memeform(request.FILES, instance=memes)

    return render(request, 'post.html', {'form': form})

def dell(request,id):
    Meme.objects.get(pk=id).delete()
    return redirect('view')