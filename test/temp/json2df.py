import json
from elasticsearch import Elasticsearch
import pkgutil
import os

__modules__ = set()

metadata = {
    "j2d": "j2d"
}

def get_module(pkg_path, modules):
    for loader, module_name, is_pkg in pkgutil.walk_packages(pkg_path):
        pkg_child_path = [pkg_path[0] + "/" + module_name]
        print(loader, module_name, is_pkg)
        if is_pkg:
            get_module(pkg_child_path, modules)
        else:
            module_name_ = ".".join(pkg_child_path[0].split("/")[1:])
            if module_name == "Task" or module_name == "SqlTask" and not module_name.endswith("Task"):
                continue
            modules.add(module_name_)
            print(module_name_)

def ex_path():
    __path__ = os.path.abspath()
    pkgutil.extend_path(__path__, __name__)

