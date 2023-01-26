load("@my_deps//:requirements.bzl", "requirement")

# py_library(
#     name = "webapp",
#     srcs = ["manage.py"],
#     deps = [requirement("django")],
# )
py_binary(
    name = "runtornado",
    main = "service.py",
    srcs = [
        "service.py",
    ],
    data = [
        "//backend/templates:templates",
    ],
    deps = [
        "//backend/backend:py_default_library",
        "//backend/todo:py_default_library",
        "//backend/backend/tornado:py_default_library",
        requirement("Django"),
        requirement("Tornado"),
        requirement("django-cors-headers"),
        requirement("django-tornado-websockets"),
        requirement("asgiref"),
        requirement("build"),
        requirement("click"),
        requirement("djangorestframework"),
        requirement("packaging"),
        requirement("pep517"),
        requirement("pyparsing"),
        requirement("pytz"),
        requirement("sqlparse"),
        requirement("tomli"),
        requirement("uvloop")
    ]
)

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
        requirement("django-tornado-websockets"),
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
#py_binary(
#    name = "manage",
#    srcs = ["manage.py"],
#    main = "manage.py",
#    visibility = ["//visibility:public"],
#    deps = [
#        "//backend/backend:py_default_library",
#        "//backend/todo:py_default_library",
#        requirement("django"),
#        requirement("django-cors-headers"),
#        requirement("asgiref"),
#        requirement("build"),
#        requirement("click"),
#        requirement("djangorestframework"),
#        requirement("packaging"),
#        requirement("pep517"),
#        requirement("pyparsing"),
#        requirement("pytz"),
#        requirement("sqlparse"),
#        requirement("tomli")
#    ],
#)
#py_binary(
#    name = "shell",
#    srcs = ["manage.py"],
#    main = "manage.py",
#    args = [
#        "shell",
#    ]
#    visibility = ["//visibility:public"],
#    deps = [
#        "//backend/backend:py_default_library",
#        "//backend/todo:py_default_library",
#        requirement("django"),
#        requirement("django-cors-headers"),
#        requirement("asgiref"),
#        requirement("build"),
#        requirement("click"),
#        requirement("djangorestframework"),
#        requirement("packaging"),
#        requirement("pep517"),
#        requirement("pyparsing"),
#        requirement("pytz"),
#        requirement("sqlparse"),
#        requirement("tomli")
#    ],
#)
