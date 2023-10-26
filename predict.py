from cog import BasePredictor, Input, Path
from typing import List


class Predictor(BasePredictor):
    def predict(self, count: int = Input(description="How yolo are you - how many images of yolo do you need???", default=1)) -> List[Path]:
        return [Path("yolo.png") for i in range(count)]
