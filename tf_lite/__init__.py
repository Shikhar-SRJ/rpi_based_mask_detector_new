import tflite_runtime.interpreter as tflite
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, 'mask_detection.tflite')


class Model(object):
    def __init__(self, model=model_path):
        self.interpreter = tflite.Interpreter(model)
        self.interpreter.allocate_tensors()

    def load_interpreter(self):
        return self.interpreter

    def input_details(self):
        return self.interpreter.get_input_details()

    def output_details(self):
        return self.interpreter.get_output_details()