import argparse
from processors.base_processor import BaseProcessor
from input import messages_as_base_10, gun_names

class Processor(BaseProcessor):
    def __init__(self, letter_index: int = 0, fallback_character: str = " ", pad_start: bool = False):
        self.letter_index = letter_index
        self.fallback_character = fallback_character
        self.pad_start = pad_start

    @classmethod
    def add_args(cls, parser: argparse.ArgumentParser):
        parser.add_argument("-li", "--letter_index", type=int)
        parser.add_argument("-fc", "--fallback_character", type=str)
        parser.add_argument("-ps", "--pad_start", action="store_true")

    def process(self) -> dict:
        result = {
            key: "".join(
                gun_names[int(val)][self.letter_index] if len(gun_names[int(val)]) > self.letter_index else self.fallback_character
                for val in values
            )
            for key, values in messages_as_base_10.items()
        }

        if result:
            max_len = max(len(val) for val in result.values())
            result = {
                key: val.rjust(max_len, " ") if self.pad_start else val.ljust(max_len, " ")
                for key, val in result.items()
            }

        return result