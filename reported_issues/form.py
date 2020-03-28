from django.forms import ModelForm
from reported_issues.models import Issue

class IssueForm(forms.ModelForm):
    # reported_file = models.CharField(max_length=200, label='Issue Category', requird=True)
    # issue_category = models.CharField(max_length=30, label='Issue Category', choices=Issue.ISSUECATEGORY, requird=True)
    # issue_message = models.CharField(max_length=400, label='Issue Category', requird=True)
    class Meta:
        model = Issue
        fields= ("issue_category", "issue_message", "reported_file",)