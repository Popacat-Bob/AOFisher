from src.controller import controller
from init import *

def main():
    control = controller(fishingModel)
    control.run()

if __name__ == '__main__':
    main()
