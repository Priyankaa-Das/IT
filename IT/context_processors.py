from .models import Service

def services_dropdown(request):
    services = Service.objects.filter(status=True).order_by('title')
    return {'nav_services': services}
