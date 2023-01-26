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
# py_binary(
#     name = "runtornado",
#     main = "asgi.py",
#     srcs = [
#         "asgi.py",
#         "settings.py",
#     ],
#     deps = [
#         "//backend/backend:py_default_library",
#         "//backend/todo:py_default_library",
#         requirement("Django"),
#         requirement("Tornado"),
#     ]
# )