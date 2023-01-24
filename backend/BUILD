load("@my_deps//:requirements.bzl", "requirement")

# py_library(
#     name = "webapp",
#     srcs = ["manage.py"],
#     deps = [requirement("django")],
# )

py_binary(
    name = "run",
    srcs = ["manage.py"],
    args = [
        "runserver",
    ],
    main = "manage.py",
    visibility = ["//visibility:public"],
    deps = [
        "//backend/backend:py_default_library",
        "//backend/todo:py_default_library",
        requirement("django"),
        requirement("django-cors-headers"),
        requirement("asgiref"),
        requirement("build"),
        requirement("click"),
        requirement("djangorestframework"),
        requirement("packaging"),
        requirement("pep517"),
        requirement("pyparsing"),
        requirement("pytz"),
        requirement("sqlparse"),
        requirement("tomli")
    ],
)
py_binary(
    name = "manage",
    srcs = ["manage.py"],
    main = "manage.py",
    visibility = ["//visibility:public"],
    deps = [
        "//backend/backend:py_default_library",
        "//backend/todo:py_default_library",
        requirement("django"),
        requirement("django-cors-headers"),
        requirement("asgiref"),
        requirement("build"),
        requirement("click"),
        requirement("djangorestframework"),
        requirement("packaging"),
        requirement("pep517"),
        requirement("pyparsing"),
        requirement("pytz"),
        requirement("sqlparse"),
        requirement("tomli")
    ],
)
py_binary(
    name = "shell",
    srcs = ["manage.py"],
    main = "manage.py",
    args = [
        "shell",
    ]
    visibility = ["//visibility:public"],
    deps = [
        "//backend/backend:py_default_library",
        "//backend/todo:py_default_library",
        requirement("django"),
        requirement("django-cors-headers"),
        requirement("asgiref"),
        requirement("build"),
        requirement("click"),
        requirement("djangorestframework"),
        requirement("packaging"),
        requirement("pep517"),
        requirement("pyparsing"),
        requirement("pytz"),
        requirement("sqlparse"),
        requirement("tomli")
    ],
)
