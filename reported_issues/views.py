from django.shortcuts import render
from reported_issues.forms import IssueForm

# Create your views here.
    def submitReport(request):
      template_name = 'polls/index.html'
      form = IssueForm(request.POST or None)
      if form.is_valid():
        # issue_message = form.cleaned_data('issue_message')
        issue = form.save(commit=False)
        # issue.email = request.user
        issue.save()
      
      # args = {'form': form, 'issue_message': issue_message}
      return render(request, template_name, context={'form': form})
