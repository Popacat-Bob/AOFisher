from .model import model, colorCaptureModel

colorCapture = colorCaptureModel((100, 100),
                                 ( 400, 400,),
                                 10
                                 )
fishingModel = model(colorCapture,
                     (255, 255, 255),
                     )