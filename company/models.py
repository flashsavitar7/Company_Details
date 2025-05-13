from django.db import models

class Company(models.Model):
    INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('health', 'Healthcare'),
        ('education', 'Education'),
    ]

    STATE_CHOICES = [
        ('lagos', 'Lagos'),
        ('abuja', 'Abuja'),
        ('rivers', 'Rivers'),
    ]

    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    company_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    country = models.CharField(max_length=100)
    website = models.URLField(blank=True)
    tax_id = models.CharField(max_length=100)

    def __str__(self):
        return self.company_email
