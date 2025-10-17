from django.core.management.base import BaseCommand
from services.models import Category, ServiceListing, Review


class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

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
        services_data = [
            {
                'service_name': 'Math Tutoring',
                'provider_name': 'Sarah Johnson',
                'contact_info': 'Call or text: (555) 123-4567',
                'email': 'sarah.math@gmail.com',
                'phone': '(555) 123-4567',
                'description': 'Experienced math tutor specializing in algebra, geometry, and calculus. Available for high school and college students. Flexible scheduling including weekends.',
                'location_area': 'Downtown Campus',
                'category': 'Tutoring',
                'price_range': '$25-40/hour'
            },
            {
                'service_name': 'Home Electrical Repairs',
                'provider_name': 'Mike\'s Electric',
                'contact_info': 'Call Mike: (555) 234-5678',
                'email': 'mike@mikeselectric.com',
                'phone': '(555) 234-5678',
                'description': 'Licensed electrician with 15 years experience. Specializing in residential electrical repairs, installations, and safety inspections. Emergency services available.',
                'location_area': 'Westside Neighborhood',
                'category': 'Home Repair',
                'price_range': 'Starting at $75/hour'
            },
            {
                'service_name': 'Dog Walking & Pet Sitting',
                'provider_name': 'Emma\'s Pet Care',
                'contact_info': 'Text preferred: (555) 345-6789',
                'email': 'emma@emmaspetcare.com',
                'phone': '(555) 345-6789',
                'description': 'Professional pet care services including daily walks, overnight pet sitting, and basic grooming. Insured and bonded. References available.',
                'location_area': 'Campus Area',
                'category': 'Pet Care',
                'price_range': '$15-25/visit'
            },
            {
                'service_name': 'Deep House Cleaning',
                'provider_name': 'Clean & Shine',
                'contact_info': 'Book online or call: (555) 456-7890',
                'email': 'info@cleanandshine.com',
                'phone': '(555) 456-7890',
                'description': 'Thorough house cleaning services including kitchens, bathrooms, living areas, and bedrooms. Eco-friendly products available. Weekly, bi-weekly, or one-time cleaning.',
                'location_area': 'Within 10 miles of downtown',
                'category': 'Cleaning',
                'price_range': '$80-150 per visit'
            },
            {
                'service_name': 'Grocery Delivery',
                'provider_name': 'Quick Delivery Co.',
                'contact_info': 'Order via app or call: (555) 567-8901',
                'email': 'orders@quickdelivery.com',
                'phone': '(555) 567-8901',
                'description': 'Fast grocery delivery from local stores. Same-day delivery available. Minimum order $25. Serving campus area and surrounding neighborhoods.',
                'location_area': 'Campus & Surrounding Areas',
                'category': 'Delivery',
                'price_range': '$5-10 delivery fee'
            },
            {
                'service_name': 'Portrait Photography',
                'provider_name': 'Creative Lens Studio',
                'contact_info': 'Email for bookings: info@creativelens.com',
                'email': 'info@creativelens.com',
                'phone': '(555) 678-9012',
                'description': 'Professional portrait photography for individuals, couples, and families. Studio and outdoor sessions available. High-resolution digital photos included.',
                'location_area': 'Studio in Eastside, travel within 20 miles',
                'category': 'Photography',
                'price_range': '$150-300 per session'
            },
            {
                'service_name': 'Birthday Party Planning',
                'provider_name': 'Party Perfect Events',
                'contact_info': 'Call Lisa: (555) 789-0123',
                'email': 'lisa@partyperfect.com',
                'phone': '(555) 789-0123',
                'description': 'Complete party planning services for birthdays, graduations, and special occasions. Includes decorations, entertainment, catering coordination, and cleanup.',
                'location_area': 'Local venues and homes',
                'category': 'Event Planning',
                'price_range': 'Starting at $200'
            },
            {
                'service_name': 'Hair Styling & Makeup',
                'provider_name': 'Beauty by Maria',
                'contact_info': 'Book appointment: (555) 890-1234',
                'email': 'maria@beautybymaria.com',
                'phone': '(555) 890-1234',
                'description': 'Professional hair styling and makeup services for special events, weddings, and everyday looks. Licensed cosmetologist with 10+ years experience.',
                'location_area': 'Home visits within 15 miles',
                'category': 'Beauty & Wellness',
                'price_range': '$60-120 per service'
            },
            {
                'service_name': 'Computer Repair & Setup',
                'provider_name': 'Tech Solutions',
                'contact_info': 'Call or text: (555) 901-2345',
                'email': 'support@techsolutions.com',
                'phone': '(555) 901-2345',
                'description': 'Computer repair, virus removal, hardware upgrades, and system setup. Specializing in laptops and desktops. On-site service available.',
                'location_area': 'Campus and nearby areas',
                'category': 'Computer Services',
                'price_range': '$50-100 per hour'
            },
            {
                'service_name': 'Airport Shuttle Service',
                'provider_name': 'Reliable Rides',
                'contact_info': 'Book online or call: (555) 012-3456',
                'email': 'bookings@reliablerides.com',
                'phone': '(555) 012-3456',
                'description': 'Reliable airport transportation with professional drivers. Clean vehicles, flight tracking, and flexible scheduling. Group rates available.',
                'location_area': 'Airport and surrounding areas',
                'category': 'Transportation',
                'price_range': '$40-80 per trip'
            }
        ]

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
        reviews_data = [
            {
                'service_listing': ServiceListing.objects.get(service_name='Math Tutoring'),
                'reviewer_name': 'John Smith',
                'rating': 5,
                'comment': 'Sarah helped my daughter improve her calculus grade from a C to an A. Very patient and explains concepts clearly. Highly recommended!'
            },
            {
                'service_listing': ServiceListing.objects.get(service_name='Math Tutoring'),
                'reviewer_name': 'Lisa Chen',
                'rating': 5,
                'comment': 'Excellent tutor! Sarah made algebra finally click for me. Flexible scheduling and great communication.'
            },
            {
                'service_listing': ServiceListing.objects.get(service_name='Home Electrical Repairs'),
                'reviewer_name': 'Robert Wilson',
                'rating': 5,
                'comment': 'Mike fixed our kitchen outlet quickly and professionally. Fair pricing and very knowledgeable. Will definitely use again.'
            },
            {
                'service_listing': ServiceListing.objects.get(service_name='Dog Walking & Pet Sitting'),
                'reviewer_name': 'Amanda Davis',
                'rating': 5,
                'comment': 'Emma takes great care of my golden retriever. My dog gets so excited when she arrives! Very reliable and trustworthy.'
            },
            {
                'service_listing': ServiceListing.objects.get(service_name='Deep House Cleaning'),
                'reviewer_name': 'Jennifer Brown',
                'rating': 4,
                'comment': 'Very thorough cleaning service. The house looked spotless after they left. Would recommend for deep cleaning needs.'
            },
            {
                'service_listing': ServiceListing.objects.get(service_name='Grocery Delivery'),
                'reviewer_name': 'David Lee',
                'rating': 4,
                'comment': 'Fast delivery and good selection. Saves me so much time during busy weeks. App is easy to use.'
            }
        ]

        for review_data in reviews_data:
            review, created = Review.objects.get_or_create(
                service_listing=review_data['service_listing'],
                reviewer_name=review_data['reviewer_name'],
                defaults=review_data
            )
            if created:
                self.stdout.write(f'Created review by {review.reviewer_name}')

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )
