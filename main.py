import importlib
import json
from pathlib import Path

PROCESSORS_DIR = Path("processors")
OUTPUT_DIR = Path("output")

def run_all_processors():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for file_path in PROCESSORS_DIR.glob("*.py"):
        if file_path.name.startswith("_") or file_path.name.startswith("base_"):
            continue

        processor_name = file_path.stem

        try:
            module = importlib.import_module(f"{PROCESSORS_DIR}.{processor_name}")
            processor = module.Processor()
            json_data = processor.process()

            output_file = OUTPUT_DIR / f"{processor_name}.json"

            with open(output_file, "w", encoding="utf-8") as file:
                json.dump(json_data, file, indent=4, ensure_ascii=False)

            print(f"Processed successfully: {processor_name}")

        except Exception as e:
            print(f"Failed to process '{processor_name}': {e}")

if __name__ == "__main__":
    run_all_processors()