import pkgutil

__modules__ = set()


def get_module(pkg_path, modules):
    for loader, module_name, is_pkg in pkgutil.walk_packages(pkg_path):
        print("loader:",loader, " module:", module_name, " is_pkg", is_pkg)
        pkg_child_path = [pkg_path[0] + "/" + module_name]
        if is_pkg:
            get_module(pkg_child_path, modules)
        else:
            module_name_ = ".".join(pkg_child_path[0].split("/")[1:])
            if module_name == "Task" or module_name == "SqlTask" and not module_name.endswith("Task"):
                continue
            modules.add(module_name_)
    print(modules)

def get_m(pkg_path, modules):
    for loader, name, is_pkg in pkgutil.iter_modules(pkg_path):
        # print("loader:", loader, " module:", module_name, " is_pkg", is_pkg)
        print "loader: {0}, name: {1:12}, is_sub_package: {2}, {3}".format(loader, name, is_pkg, modules)

__path__ = "./"
__modules__ = "./"

get_m(__path__, __modules__)
# get_module(__path__, __modules__)