from django.contrib import admin

# Register your models here.
from reported_issues.models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_id', 'email', 'submitted_date', 'issue_category', 'issue_message', 'reported_file')
    # readonly_fields = ('issue_id', 'email', 'submitted_date', 'issue_category', 'issue_message', 'reported_file')
    search_fields = ('email', 'issue_message','reported_file')
    list_filter = ('email', 'submitted_date', 'issue_category', 'reported_file')
   
admin.site.register(Issue, IssueAdmin)
