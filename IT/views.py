from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Blog, Team
from .models import Service , CaseStudy, CaseStudyCategory , ContactMessage
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm







def index(request):
    teams = Team.objects.all()
    data = Blog.objects.all().order_by('-id')

    context = {
        'data':data,
        'teams': teams,
    }
    return render(request, 'index.html', context)


def about(request):
    teams = Team.objects.all()
    

    context = {
        
        'teams': teams,
    }
    return render(request, 'about.html', context)






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





def case_study_list(request):
    case_studies = CaseStudy.objects.filter(status=True).order_by('-published')
    categories = CaseStudyCategory.objects.all()
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(CaseStudyCategory, slug=category_slug)
        case_studies = case_studies.filter(category=category)
    
    context = {
        'case_studies': case_studies,
        'categories': categories,
        'current_category': category_slug,
    }
    return render(request, 'case_study/case_study_list.html', context)


def case_study_detail(request, slug):
    case_study = get_object_or_404(CaseStudy, slug=slug, status=True)
    related_studies = CaseStudy.objects.filter(
        status=True
    ).exclude(id=case_study.id).order_by('-published')[:3]
    
    context = {
        'case_study': case_study,
        'related_studies': related_studies,
    }
    return render(request, 'case_study/case_study_detail.html', context)


def faq(request):
	return render(request, 'faqs.html')

def testimonials(request):
	return render(request, 'testimonials.html')





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact_message = form.save()
            
            # Show success message
            messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
            
            # Optional: Send email notification
            # send_mail(
            #     f'New Contact Message from {contact_message.name}',
            #     contact_message.message,
            #     contact_message.email,
            #     ['your-email@example.com'],
            #     fail_silently=False,
            # )
            
            # Redirect to avoid form resubmission
            return redirect('contact_success')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)

def contact_success_view(request):
    return render(request, 'contact/contact_success.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_of_service(request):  
    return render(request, 'terms_of_service.html')