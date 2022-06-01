import importlib.util
import os


def create_db(app, dir):
    try:
        lst = os.listdir("app/" + dir)
    except OSError:
        print("NO SE PUDIERON CARGAR LAS BLUEPRINTS")
    else:
        for name_route in lst:
            if name_route != "__pycache__":
                name_class = name_route.split(".py")[0]
                module = importlib.import_module("app." + dir + "." + name_class)
                app.register_blueprint(getattr(module, name_class))
