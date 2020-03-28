# from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.
class Issue(models.Model): 
    issue_id = models.AutoField(primary_key=True)
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=400)
    submitted_date = models.DateTimeField(auto_now_add=True, blank=None, null=None)
    ISSUECATEGORY = [
        ('IFC Issue', 'IFC Issue'),
        ('Billing Issue', 'Billing Issue'),
        ('Other', 'Other'),
    ]
    issue_category = models.CharField(max_length=30, choices=ISSUECATEGORY, blank=False)
    issue_message = models.CharField(max_length=400, blank=False)
    reported_file = models.CharField(max_length=200, blank=False)