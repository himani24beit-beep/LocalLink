from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    """Model for service categories like 'Tutoring', 'Home Repair', 'Pet Care'"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class ServiceListing(models.Model):
    """Model for service listings"""
    service_name = models.CharField(max_length=200)
    provider_name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    location_area = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='services')
    price_range = models.CharField(max_length=100, blank=True, help_text="e.g., '$20-50/hour', 'Starting at $30'")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.service_name} by {self.provider_name}"
    
    @property
    def average_rating(self):
        """Calculate average rating from reviews"""
        reviews = self.reviews.all()
        if reviews:
            return round(sum(review.rating for review in reviews) / len(reviews), 1)
        return 0
    
    @property
    def review_count(self):
        """Get total number of reviews"""
        return self.reviews.count()


class Review(models.Model):
    """Model for service reviews"""
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    service_listing = models.ForeignKey(ServiceListing, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=RATING_CHOICES, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.rating}-star review for {self.service_listing.service_name} by {self.reviewer_name}"
