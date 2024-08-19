import pkgutil
import importlib
from libs.base import Base


def main():
    for finder, name, _ in pkgutil.iter_modules(['modules']):
        try:
            importlib.import_module('{}.{}'.format(finder.path, name))
        except Exception as e:
            print(f'Can not import {name}')

    for cls in Base.__subclasses__():

        instance = cls()
        instance.Run()

if __name__ == '__main__':
    main()