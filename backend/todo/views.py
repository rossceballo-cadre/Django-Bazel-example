from django.shortcuts import render
from tornado.web import RequestHandler

from .models import Todo


# Create your views here.

from django.http import HttpResponse


def hello(request):
    """A test view to assure django is responsing."""
    return HttpResponse("Hello from django")


def todo_list(request):
    todos = Todo.objects.all()
    for e in todos:
        print(e.title)
    return render(request, "todo_list.html", {"todos": todos})


class Todo_list(RequestHandler):
    template_name = "todo_list.html"

    def get(self):
        todos = Todo.objects.all()
        # TemplateModule.render(self.template_name, {"todos": todos})
        self.write(todos)
        # return render(request, self.template_name, {"todos": todos})
