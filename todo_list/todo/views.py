from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import task, TaskForm
from django.views.generic import FormView

# Create your views here

def list_todo(request):
    return render(
        request, template_name='page.html',
        context= {'tasks': task.objects.all()}
    )

def done(request):
    return render(
        request, template_name='done.html',
        context= {"tasks": task.objects.all()}
    )

def mark_task_done(request, task_id):
    try:
        task1 = task.objects.get(id=task_id)
        task1.is_done = True
        task1.save()
        return JsonResponse({'success': True})
    except task.DoesNotExist:
        return JsonResponse({'success': False})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name_task']
            date_created = form.cleaned_data['date_created_task']

            new_task = task(name=name, date_created=date_created, is_done=False)
            new_task.save()

            return redirect('list_todo')  # Redirect to a page that lists tasks
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})


def delete_task(request, task_id):
    Task = get_object_or_404(task, id=task_id)

    # Delete the task from the database
    Task.delete()

    # Return a JSON response indicating success
    return JsonResponse({'success': True})