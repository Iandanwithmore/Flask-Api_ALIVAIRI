import functools
import inspect
import traceback
from timeit import default_timer as timer

from flask import abort, current_app, jsonify, request


def user_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if current_app.config["SECURE"]:
            if "CCODUSU" not in request.args:
                current_app.logger.info(
                    f"{request.args['CCODUSU']}:'SE INTENTO INGRESAR CON EL SIGUEINTE CODIGO DE USUARIO'"
                )
                abort(400, "USUARIO NO DENODINIDO!")
        secure_function.attrib = request.args["CCODUSU"]
        return func(*args, **kwargs)

    return secure_function


def exception_handler_request(func) -> object:
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        R1 = {"OK": 0, "DATA": ""}
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("-" * 60)
            print(e.__class__.__name__)
            traceback.print_exc()
            print("-" * 60)
            if e.__class__.__name__ == "AttributeError":
                R1["DATA"] = None
                return jsonify(R1), 400
            elif e.__class__.__name__ in [
                "ValueError",
                "AssertionError",
                "KeyError",
                "TypeError",
            ]:
                R1["DATA"] = str(e)
                return jsonify(R1), 400
            else:
                R1["DATA"] = str(e)
                return jsonify(R1), 500

    return inner_function


def exception_handler(error_response):
    def factory_exception(func):
        @functools.wraps(func)
        def inner_function(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print("-" * 60)
                print(f"CALLER: {inspect.stack()[1][2]}-{inspect.stack()[1][3]}()")
                print(e.__class__.__name__)
                traceback.print_exc()
                print("-" * 60)
                if e.__class__.__name__ in [
                    "ValueError",
                    "AssertionError",
                    "KeyError",
                    "TypeError",
                ]:
                    print(str(e))
                return error_response

        return inner_function

    return factory_exception


def monitor_elapsed_time(func):
    def wrapper(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        print(f"Time elapsed: {timer() - start}")

    return wrapper
