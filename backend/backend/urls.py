from django.urls import path, include

from todo import views


# urlpatterns = [
#     path("todo", views.todo_list, name="todo_list"),
# ]
urlpatterns = [
    # "",
    path("", views.hello),
    path("todo", views.todo_list),
]
