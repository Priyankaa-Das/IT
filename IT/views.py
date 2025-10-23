from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Blog, Team
from .models import Service
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm



def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')






def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team/team_list.html', {'teams': teams})

def team_detail(request, slug):
    member = get_object_or_404(Team, slug=slug)
    return render(request, 'team/team_detail.html', {'member': member})



def blog(request):
    data = Blog.objects.all().order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'blog/blogs.html', context)

def blog_detail(request, pk):
    data = Blog.objects.get(slug=pk)
    data2 = Blog.objects.all().order_by('-id')[:7]
    context = {
        'data':data,
        'data2':data2,
    }
    return render(request, 'blog/blog_detail.html', context)




def service_list(request):
    data = Service.objects.all().order_by('-id')
    context = {
        'data':data,
    }
    return render(request, 'services/services.html', context)



def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    data2 = Service.objects.all().order_by('-id')[:7]
    
    # If you want to show recent/other services
    recent_services = Service.objects.filter(status=True).exclude(id=service.id).order_by('-created_at')[:5]
    
    context = {
        'service': service,
        'recent_services': recent_services,
        'data2': data2,
    }
    return render(request, 'services/service_detail.html', context)





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home:contact')  # redirect to the same page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})