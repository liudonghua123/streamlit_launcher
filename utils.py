from os.path import join, normpath, exists, dirname
import pkgutil

def get_package_dir_path(package_name):
    """Return package directory path from its name."""
    loader = pkgutil.get_loader(package_name)
    return loader.path.replace("__init__.py", "")

def build_package_datas_item(package_name, sub_path, dir_mode=True):
    package_file_path = normpath(join(get_package_dir_path(package_name), sub_path))
    if not exists(package_file_path):
        print(f"WARNING: {package_file_path} does not exist")
    if dir_mode:
        return (package_file_path, normpath(join(package_name, sub_path)))
    return (package_file_path, normpath(join(package_name, dirname(sub_path))))