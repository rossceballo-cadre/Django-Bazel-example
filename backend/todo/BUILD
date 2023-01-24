load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")
package(default_visibility = ["//visibility:public"])


py_library(
    name = "py_default_library",
    srcs = [
        "__init__.py",
        "admin.py",
        "apps.py",
        "models.py",
        "tests.py",
        "views.py",
    ],
    deps = [
        "//backend/todo/migrations:py_default_library",
        requirement("Django"),
    ],
)