from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .forms import TodoCreateForm
# Create your views here.
def home(request):
    person = { 'name' : 'Hossein'}
    return render(request, 'home.html', context=person)

def say_hello(request):
    return HttpResponse(" Hello MFs!")

def say_bye(request):
    return render(request, 'bye.html')

def read_Todo(request):
    all_data = Todo.objects.all()
    return render(request, 'read_Todo.html', {'all':all_data})

def create(request):
    """
    if the method is Post, it means the user submit the data
    otherwise they are only in the create page!
    """
    if request.method == 'POST':
        """
        This line means that with request module I want the data
        that user send by Post method and put them inside the class
        I created for my specific form to validate the data that user
        sent to me with django form tools for validation!
        """
        form = TodoCreateForm(request.POST) 
        if form.is_valid :
            cd = (form.cleaned_data) # data after getting validated in dictionary
            Todo.objects.create(
                title=cd['title'],
                body=cd['body'],
                body=cd['created']
                ) 
            # The first <title> is for the model the second is for the form
            # The first <body> is for the model the second is for the form
            # The first <created> is for the model the second is for the form
    else:
        form = TodoCreateForm()
        return render(request, 'create.html', {'form':form})
