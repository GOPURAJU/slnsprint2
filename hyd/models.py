from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
import logging
import datetime
from django.core.exceptions import ValidationError
import re




def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Only letters are allowed.')
    

    
def validate_mobile_number(value):
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, value) or len(value) < 10:
        raise ValidationError('Invalid mobile number format. Must be at least 10 digits long.')
    if len(value) > 15:
        raise ValidationError('Mobile number cannot be more than 15 digits long.')






















class Ticket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('New', 'New'),
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]



    issue_CHOICES = [
        ('personal loan', 'Personal Loan'),
        ('educational loan', 'Educational Loan'),
        ('car loan', 'Car Loan'),
        ('business loan', 'Business Loan'),
        ('Loan Againest Property', 'Loan Againest Property'),
        ('CreditCard', 'CreditCard'),
        ('Insurance', 'Insurance'),
        ('Other Loan', 'Other Loan')
    ]

    # Fields for the CustomerTicket model
    ticket_id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100,validators=[validate_only_letters])
    phone_number = models.CharField(max_length=10,validators=[validate_mobile_number])
    Issue_type = models.CharField(max_length=100,choices=issue_CHOICES)  # Type of the issue
    description = models.TextField()  # Detailed description of the issue
    related_application_number = models.CharField(max_length=100, blank=True, null=True)  # Related application number (optional)
    supporting_documents = models.FileField(upload_to='supporting_documents/', blank=True, null=True)  # Uploaded documents (optional)
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='New')  # Current status of the ticket
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the ticket was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the ticket was last updated

    def __str__(self):
        return f'Ticket #{self.ticket_id} - {self.Issue_type}'







# //////////////////////     DSA    ///////////////////////////////////////////////





class DSATicket(models.Model):
    # Defining choices for Issue Type
    ISSUE_TYPE_CHOICES = [
    ('Technical', 'Technical'),
    ('Billing', 'Billing'),
    ('General', 'General'),
    ('Personal', 'Personal'),
    ('others','others')
    ]


    TICKET_STATUS_CHOICES = [
        ('NEW', 'new'),
        ('open', 'open'),
        ('In Progress', 'In Progress'),
        ('resolved', 'resolved'),
    ]
    
    ticket_id = models.AutoField(primary_key=True)  
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='new',choices=TICKET_STATUS_CHOICES)  # You can use choices here as well
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25,validators=[validate_only_letters])
    phone_number = models.CharField(max_length=10)
    
    def __str__(self):
        return f"Ticket {self.ticket_id} - {self.issue_type}"




# ///////////////////////////////  franchisee ////////////////////////////////////////////////////////





ISSUE_TYPE_CHOICES = [
    ('Technical', 'Technical'),
    ('Billing', 'Billing'),
    ('General', 'General'),
    ('Personal', 'Personal'),
    ('others', 'others')
]

TICKET_STATUS_CHOICES = [
    ('new', 'new'),
    ('Open', 'Open'),
    ('In Progress', 'In Progress'),
    ('Resolved', 'Resolved'),
]

class FranchiseeTicket(models.Model):
    ticket_id = models.AutoField(primary_key=True)  
    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, default='new', choices=TICKET_STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100,validators=[validate_only_letters])
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return f'Ticket {self.ticket_id} - {self.issue_type}'

    