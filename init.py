from model import model, colorCaptureModel
from view import view

colorCapture = colorCaptureModel((100, 100),
                                 ( 400, 400,),
                                 10
                                 )
fishingModel = model(colorCapture,
                     (255, 255, 255),
                     )

view = view()