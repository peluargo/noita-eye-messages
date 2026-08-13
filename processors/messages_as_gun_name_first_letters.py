from processors.base_processor import BaseProcessor
from input import messages_as_base_10, gun_names

class Processor(BaseProcessor):
    def process(self) -> dict:
        return {
            key: [gun_names[int(val)][0] for val in values]
            for key, values in messages_as_base_10.items()
        }
