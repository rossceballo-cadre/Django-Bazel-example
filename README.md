# Working Django bazel concept

### How to Run it
#### Run with Django no Tornado
```
bazel run //backend:run
```

#### Run with Tornado
```
bazel run //backend:runtornado
```

#### Run with bazel watcher
[iBazel](https://github.com/bazelbuild/bazel-watcher) restarts the bazel session whenever you make a change to your src files.
```
ibazel run //backend:runtornado
```

### What is left to add
1. Add a react frontend
1. Add linting through bazel
1. Add testing through bazel
