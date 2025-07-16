import os
from src.model import model, colorCaptureModel

def init_config():

    if not os.path.exists('data/config.json'):
        try:
            with open('baseplates/config.json', 'r') as origin:
                base = origin.read()

            with open('data/config.json', 'w') as new:
                new.write(base)

        except Exception as e:
            raise SystemError(e)


colorCapture = colorCaptureModel((100, 100),
                                 ( 400, 400,),
                                 10
                                 )
fishingModel = model(colorCapture,
                     (255, 255, 255),
                     )