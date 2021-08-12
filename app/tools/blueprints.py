import importlib
import os


def discover_blueprints(path: str) -> list:
    """ This method used to load blueprints from given path """

    blueprints = list()
    dir_name = os.path.basename(path)
    packages = os.listdir(os.path.join(path, "blueprints"))

    for package in packages:
        if str(package).endswith(".py") and str(package) != "__init__.py":
            package = str(package).replace(".py", "")
            module_name = f"{dir_name}.blueprints.{package}"
            module = importlib.import_module(module_name)
            module_blueprints = [bp for bp in dir(
                module) if bp.endswith("_blueprint")]

            for mb in module_blueprints:
                blueprints.append(getattr(module, mb))

    return blueprints
