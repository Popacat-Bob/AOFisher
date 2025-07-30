import os
from src.model import model, colorCaptureModel
import json

def init_config():

    if not os.path.exists('data/config.json'):
        try:
            with open('baseplates/config.json', 'r') as origin:
                base = origin.read()

            with open('data/config.json', 'w') as new:
                new.write(base)

        except Exception as e:
            raise SystemError(e)


def init_models():

    try:
        with open('data/config.json', 'r') as f:
            data = json.load(f)

        captureSettingsPrompt = data['ColorCaptureSettings']
        CaptureModelPrompt = colorCaptureModel(
            captureSettingsPrompt['topLeft'],
            captureSettingsPrompt['bottomRight'],
            captureSettingsPrompt['tolerance']
        )

        captureSettingsNotify = data['ColorCaptureSettings1']
        captureModelNotify = colorCaptureModel(
            captureSettingsNotify['topLeft'],
            captureSettingsNotify['bottomRight'],
            captureSettingsNotify['tolerance']
        )

        fishModelSettings = data['FisherModelSettings']
        fishingModel = model(
            capturePrompt=CaptureModelPrompt,
            captureNotify=captureModelNotify,
            colorPrompt=fishModelSettings['color'],
            colorNotify=fishModelSettings['colorNotify'],
            scanDelay= fishModelSettings['scan_delay'],
            clickDelay= fishModelSettings['click_delay'],
            postFishDelay= fishModelSettings['post_fish_delay'],
            clicks= fishModelSettings['clicks'],
            timeEatInterval= fishModelSettings['time_eat_interval'],
            brewEatInterval= fishModelSettings['brew_eat_interval'],
            resetDuration= fishModelSettings['reset_duration'],
        )

    except Exception as e:
        raise SystemError(e)

    return fishingModel