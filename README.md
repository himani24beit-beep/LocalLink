# LocalLink - Community Service Directory 🛠️

A simple, hyperlocal directory for finding local services, like tutors, electricians, or pet sitters in your neighborhood or college campus.

## Features

- **Service Listings**: Create, read, update, and delete service listings
- **Categories**: Organize services by type (Tutoring, Home Repair, Pet Care, etc.)
- **Search & Filter**: Find services by name, location, or category
- **Reviews**: Rate and review services you've used
- **Responsive Design**: Beautiful UI built with Tailwind CSS
- **Admin Interface**: Easy management through Django admin

## Technology Stack

- **Backend**: Django 5.2.7
- **Frontend**: HTML templates with Tailwind CSS
- **Database**: SQLite (default)
- **Python**: 3.12+

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

3. **Populate Sample Data** (optional):
   ```bash
   python manage.py populate_data
   ```

4. **Create Admin User**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Main site: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/
     - Username: `admin`
     - Password: `admin123`

## Database Models

### Category
- `name`: Category name (e.g., "Tutoring", "Home Repair")
- `description`: Category description
- `created_at`: Creation timestamp

### ServiceListing
- `service_name`: Name of the service
- `provider_name`: Name of the service provider
- `contact_info`: Primary contact method
- `email`: Email address (optional)
- `phone`: Phone number (optional)
- `description`: Detailed service description
- `location_area`: Service area/location
- `category`: Foreign key to Category
- `price_range`: Pricing information (optional)
- `is_available`: Service availability status
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Review
- `service_listing`: Foreign key to ServiceListing
- `reviewer_name`: Name of the reviewer
- `rating`: Rating from 1-5 stars
- `comment`: Review text
- `created_at`: Creation timestamp

## Key Features

### For Service Providers
- List your services with detailed descriptions
- Set pricing and availability
- Manage your contact information
- Update or delete your listings

### For Service Seekers
- Browse services by category
- Search for specific services or locations
- Read reviews from other users
- Contact service providers directly
- Leave reviews after using services

### Search & Filtering
- Search by service name, provider name, or description
- Filter by category
- Filter by location
- Paginated results for better performance

## Sample Data

The application comes with sample data including:
- 10 service categories
- 10 sample service listings
- 6 sample reviews

Run `python manage.py populate_data` to populate the database with sample data.

## Admin Interface

Access the Django admin interface at `/admin/` to:
- Manage categories, services, and reviews
- View analytics and user activity
- Moderate content if needed

## Project Structure

```
LocalLink/
├── locallink/           # Django project settings
├── services/            # Main application
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── admin.py        # Admin configuration
│   ├── urls.py         # URL patterns
│   └── management/     # Custom management commands
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   └── services/       # Service-specific templates
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Future Enhancements

- User authentication and profiles
- Direct messaging between users
- Photo uploads for services
- Map integration for location display
- Email notifications
- Mobile app development
- Advanced search filters
- Service booking system
