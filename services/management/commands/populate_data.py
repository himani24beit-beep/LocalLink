from django.core.management.base import BaseCommand
from services.models import Category, ServiceListing, Review
import random


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        indian_service_locations = [
            {"city": "Mumbai", "lat": 19.0760, "lng": 72.8777},
            {"city": "Delhi", "lat": 28.6139, "lng": 77.2090},
            {"city": "Bangalore", "lat": 12.9716, "lng": 77.5946},
            {"city": "Chennai", "lat": 13.0827, "lng": 80.2707},
            {"city": "Hyderabad", "lat": 17.3850, "lng": 78.4867},
            {"city": "Kolkata", "lat": 22.5726, "lng": 88.3639},
            {"city": "Pune", "lat": 18.5204, "lng": 73.8567},
            {"city": "Ahmedabad", "lat": 23.0225, "lng": 72.5714},
            {"city": "Jaipur", "lat": 26.9124, "lng": 75.7873},
            {"city": "Lucknow", "lat": 26.8467, "lng": 80.9462},
        ]

        indian_names = [
            "Amit Sharma", "Priya Patel", "Vikram Singh", "Neha Gupta", "Ravi Kumar",
            "Sunita Reddy", "Ankit Mehra", "Aishwarya Rao", "Sandeep Nair", "Swati Desai"
        ]
        indian_phones = [
            "+91-9876543210", "+91-8887766554", "+91-9012345678", "+91-9898989898", "+91-9123456789",
            "+91-7001234567", "+91-9090909090", "+91-9955443322", "+91-9988776655", "+91-8001234567"
        ]

        # Create categories
        categories_data = [
            {'name': 'Tutoring', 'description': 'Academic tutoring and educational services'},
            {'name': 'Home Repair', 'description': 'Home improvement and repair services'},
            {'name': 'Pet Care', 'description': 'Pet sitting, walking, and grooming services'},
            {'name': 'Cleaning', 'description': 'House cleaning and maintenance services'},
            {'name': 'Delivery', 'description': 'Local delivery and pickup services'},
            {'name': 'Photography', 'description': 'Photography and videography services'},
            {'name': 'Event Planning', 'description': 'Party and event planning services'},
            {'name': 'Beauty & Wellness', 'description': 'Hair, makeup, and wellness services'},
            {'name': 'Computer Services', 'description': 'Computer repair and tech support'},
            {'name': 'Transportation', 'description': 'Ride sharing and transportation services'},
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create sample services
        services_data = []
        for idx, cat in enumerate(categories_data):
            provider_name = indian_names[idx % len(indian_names)]
            phone = indian_phones[idx % len(indian_phones)]
            loc = indian_service_locations[idx % len(indian_service_locations)]
            services_data.append({
                'service_name': f'{cat["name"]} Service',
                'provider_name': provider_name,
                'contact_info': f'Contact: {phone}',
                'email': f'{provider_name.replace(" ","").lower()}@example.com',
                'phone': phone,
                'description': f"Top-rated {cat['name'].lower()} offered by {provider_name} in {loc['city']}.",
                'location_area': loc['city'],
                'latitude': loc['lat'],
                'longitude': loc['lng'],
                'category': cat['name'],
                'price_range': '₹500-2000'
            })

        for service_data in services_data:
            category_name = service_data.pop('category')
            service, created = ServiceListing.objects.get_or_create(
                service_name=service_data['service_name'],
                provider_name=service_data['provider_name'],
                defaults={
                    **service_data,
                    'category': categories[category_name]
                }
            )
            if created:
                self.stdout.write(f'Created service: {service.service_name}')

        # Create sample reviews
        indian_reviewer_names = [
            "Harshita Sharma", "Manish Jain", "Ritu Desai", "Arjun Patel", "Roshni Singh",
            "Dhruv Khanna", "Akanksha Verma", "Deepak Joshi", "Aarav Mehra", "Priya Reddy"
        ]
        indian_comments = [
            "Excellent service, highly recommended!",
            "Quick response and very professional.",
            "Very helpful and friendly provider.",
            "Easy to communicate and the work was great.",
            "They really care about the customer.",
            "Arrived on time and completed as promised.",
            "Best experience I've had for this type of service.",
            "Affordable and reliable.",
            "Made the process very smooth.",
            "Will definitely use again!"
        ]
        reviews_data = []
        for idx, service in enumerate(ServiceListing.objects.all()):
            # At least 2 reviews, up to 4, per service
            for rev in range(2):
                reviews_data.append({
                    'service_listing': service,
                    'reviewer_name': indian_reviewer_names[(idx+rev)%len(indian_reviewer_names)],
                    'rating': random.randint(4,5),
                    'comment': indian_comments[(idx+rev)%len(indian_comments)]
                })

        for review_data in reviews_data:
            Review.objects.update_or_create(
                service_listing=review_data['service_listing'],
                reviewer_name=review_data['reviewer_name'],
                defaults=review_data
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
