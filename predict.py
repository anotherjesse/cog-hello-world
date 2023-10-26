from cog import BasePredictor, Input, Path
from typing import List


class Predictor(BasePredictor):
    def setup(self):
        self.prefix = "hello"

    def predict(self, count: int = Input(description="How yolo are you?", default=1)) -> List[Path]:
        return [Path("yolo.png") for i in range(count)]
