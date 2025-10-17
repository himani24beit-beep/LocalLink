from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
import uuid
from .models import ServiceListing, Category, Review
from .forms import ServiceListingForm, ReviewForm


def is_service_owner(request, service):
    """Check if the current session owns this service"""
    if 'owned_services' not in request.session:
        return False
    return str(service.pk) in request.session['owned_services']


def home(request):
    """Home page showing featured services and categories"""
    featured_services = ServiceListing.objects.filter(is_available=True).order_by('-created_at')[:6]
    categories = Category.objects.all()[:8]
    
    context = {
        'featured_services': featured_services,
        'categories': categories,
    }
    return render(request, 'services/home.html', context)


def service_list(request):
    """List all services with search and filter functionality"""
    services = ServiceListing.objects.filter(is_available=True)
    categories = Category.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        services = services.filter(
            Q(service_name__icontains=search_query) |
            Q(provider_name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location_area__icontains=search_query)
        )
    
    # Category filter
    category_id = request.GET.get('category')
    if category_id:
        services = services.filter(category_id=category_id)
    
    # Location filter
    location = request.GET.get('location')
    if location:
        services = services.filter(location_area__icontains=location)
    
    # Pagination
    paginator = Paginator(services, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_location': location,
    }
    return render(request, 'services/service_list.html', context)


def service_detail(request, pk):
    """Detail view for a specific service"""
    service = get_object_or_404(ServiceListing, pk=pk)
    reviews = service.reviews.all()
    
    # Handle review form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.service_listing = service
            review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('service_detail', pk=pk)
    else:
        form = ReviewForm()
    
    context = {
        'service': service,
        'reviews': reviews,
        'form': form,
        'is_owner': is_service_owner(request, service),
    }
    return render(request, 'services/service_detail.html', context)


def create_service(request):
    """Create a new service listing"""
    if request.method == 'POST':
        form = ServiceListingForm(request.POST)
        if form.is_valid():
            service = form.save()
            # Generate a unique owner key and store it in session
            owner_key = str(uuid.uuid4())
            if 'owned_services' not in request.session:
                request.session['owned_services'] = {}
            request.session['owned_services'][str(service.pk)] = owner_key
            request.session.save()
            
            messages.success(request, 'Your service listing has been created successfully!')
            messages.info(request, f'Your service has been created. You can edit or delete it using your browser session. Keep this page bookmarked to manage your listing.')
            return redirect('service_detail', pk=service.pk)
    else:
        form = ServiceListingForm()
    
    context = {
        'form': form,
        'title': 'List Your Service',
    }
    return render(request, 'services/service_form.html', context)


def update_service(request, pk):
    """Update an existing service listing"""
    service = get_object_or_404(ServiceListing, pk=pk)
    
    # Check ownership
    if not is_service_owner(request, service):
        messages.error(request, 'You can only edit services that you created.')
        return redirect('service_detail', pk=pk)
    
    if request.method == 'POST':
        form = ServiceListingForm(request.POST, instance=service)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Your service listing has been updated successfully!')
            return redirect('service_detail', pk=pk)
    else:
        form = ServiceListingForm(instance=service)
    
    context = {
        'form': form,
        'service': service,
        'title': 'Update Your Service',
    }
    return render(request, 'services/service_form.html', context)


def delete_service(request, pk):
    """Delete a service listing"""
    service = get_object_or_404(ServiceListing, pk=pk)
    
    # Check ownership
    if not is_service_owner(request, service):
        messages.error(request, 'You can only delete services that you created.')
        return redirect('service_detail', pk=pk)
    
    if request.method == 'POST':
        service.delete()
        # Remove from session
        if 'owned_services' in request.session:
            request.session['owned_services'].pop(str(service.pk), None)
            request.session.save()
        messages.success(request, 'Your service listing has been deleted successfully!')
        return redirect('service_list')
    
    context = {
        'service': service,
    }
    return render(request, 'services/service_confirm_delete.html', context)


def category_services(request, category_id):
    """Show services for a specific category"""
    category = get_object_or_404(Category, pk=category_id)
    services = ServiceListing.objects.filter(category=category, is_available=True)
    
    # Search within category
    search_query = request.GET.get('search', '')
    if search_query:
        services = services.filter(
            Q(service_name__icontains=search_query) |
            Q(provider_name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    
    # Pagination
    paginator = Paginator(services, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'services/category_services.html', context)
