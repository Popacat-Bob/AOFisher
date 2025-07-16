from model import model
from view import view

class controller:
    def __init__(self, root, model: model):
        self.run = model.run
        self.view = view(root, self)
