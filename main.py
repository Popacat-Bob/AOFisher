#!/usr/bin/env python3

from src.controller import controller
from init import *

def main():
    init_config()
    model = init_models()
    control = controller(model)
    control.run()

if __name__ == '__main__':
    main()