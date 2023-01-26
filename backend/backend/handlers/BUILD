load("@my_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_library")
package(default_visibility = ["//visibility:public"])

py_library(
    name = "py_default_library",
    srcs = [
        "__init__.py",
        "asgi_handler.py",
    ],
    deps = [
        ":mixins"
        requirement("django"),
        requirement("tornado"),
    ],
)
py_library(
    name = "mixins",
    srcs = [
        "mixins.py",
    ],
    deps = [
        requirement("typing"),
        requirement("http"),
        requirement("tornado"),
    ],
)