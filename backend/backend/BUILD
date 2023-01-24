load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")
package(default_visibility = ["//visibility:public"])


py_library(
    name = "py_default_library",
    srcs = [
        "__init__.py",
        "settings.py",
        "urls.py",
        "wsgi.py",
    ],
    deps = [
        requirement("Django"),
        requirement("pytz"),
        requirement("sqlparse"),
    ],
)