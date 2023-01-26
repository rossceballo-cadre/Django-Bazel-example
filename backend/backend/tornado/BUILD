load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library", "py_binary")
package(default_visibility = ["//visibility:public"])
py_library(
    name = "py_default_library",
    srcs = [
        "apps.py",
        "application.py"
    ],
    deps = [
        requirement("django"),
        requirement("tornado"),
    ],
)

py_binary(
    name = "service",
    srcs = [
        "run_tornado.py",
    ],
    main = "run_tornado.py",
    visibility = ["//visibility:public"],
    data = [
        "//backend/templates:templates",
    ],
    deps = [
        "//backend/backend:py_default_library",
        "//backend/todo:py_default_library",
        "//backend/backend/preload:py_default_library",
        "//backend/backend/handlers:py_default_library",
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