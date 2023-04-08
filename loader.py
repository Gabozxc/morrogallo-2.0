import importlib
import os

def discover_modules():
    modules_dir = os.path.join(os.path.dirname(__file__), 'modules')
    modules = []
    for filename in os.listdir(modules_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = os.path.splitext(filename)[0]
            module = importlib.import_module(f'modules.{module_name}')
            modules.append(module)
    return modules

def register_handlers(bot):
    modules = discover_modules()
    for module in modules:
        for name, obj in module.__dict__.items():
            if callable(obj) and name.startswith('register_'):
                obj(bot)