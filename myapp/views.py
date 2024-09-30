from django.shortcuts import render

# Create your views here.
def task_view(request):
    dynamic_data = "This is some dynamic content!"
    return render(request, 'myapp/task.html', {'dynamic_data': dynamic_data})