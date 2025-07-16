from controller import controller
from init import fishingModel, view

def main():
    control = controller(fishingModel, view)
    control.run()

if __name__ == '__main__':
    main()
