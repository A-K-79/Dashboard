from django.db import models

# Create your models here.
    
class Visitor(models.Model):
    visitor_id = models.PositiveIntegerField(unique=True)  # Unique ID
    visitor_name = models.CharField(max_length=100)
    visitor_email = models.EmailField()
    category = models.CharField(max_length=50)
    document = models.FileField(upload_to='visitor_documents/', null=True, blank=True)  # Document upload
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    designated_attendee = models.CharField(max_length=100)

    # There are 9 inputs in the form, hence 9 items.

    def __str__(self):
        return self.visitor_name
