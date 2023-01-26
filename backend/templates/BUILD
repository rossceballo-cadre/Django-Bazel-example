
# genrule(
#     name = "temp",
#     srcs = ":templates",
# )
# exports_files([":templates"])
filegroup(
    visibility = ["//visibility:public"],
    name = "templates",
    srcs = glob(
        ["**/*"],
        exclude = [
            ".git/**",
            "bazel-*/**",
            "BUILD",
            "WORKSPACE",
            "scripts/**",
            "*.swp",
            "LICENSE",
            "CONTRIBUTING",
            "production/**",
            "README.md",
            "secret",
        ],
    ),
)