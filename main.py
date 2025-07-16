from controller import controller
from init import fishingModel

def main():
    control = controller(fishingModel)
    control.run()

if __name__ == '__main__':
    main()
