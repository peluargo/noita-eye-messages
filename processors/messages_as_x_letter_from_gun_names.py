from processors.base_processor import BaseProcessor
from input import messages_as_base_10, gun_names

LETTER_INDEX = 4 # 0-10 (longest gun name is 10 characters long)
FALLBACK_CHARACTER = " " # character to use when the gun name is too short

class Processor(BaseProcessor):
    def process(self) -> dict:
        return {
            key: "".join(
                gun_names[int(val)][LETTER_INDEX] if len(gun_names[int(val)]) > LETTER_INDEX else FALLBACK_CHARACTER
                for val in values
            )
            for key, values in messages_as_base_10.items()
        }
