import argparse
import importlib
import inspect
import json
from pathlib import Path

PROCESSORS_DIR = Path("processors")
OUTPUT_DIR = Path("output")

def run_processor(processor_name, cli_args):
    print(f"\n[DEBUG] Processador: {processor_name}")
    print(f"[DEBUG] CLI Args recebidos: {cli_args}")

    try:
        module = importlib.import_module(f"{PROCESSORS_DIR}.{processor_name}")
        processor_class = module.Processor

        parser = argparse.ArgumentParser(allow_abbrev=False)
        if hasattr(processor_class, "add_args"):
            processor_class.add_args(parser)
            print("[DEBUG] add_args encontrado e executado.")
        else:
            print("[DEBUG] AVISO: add_args NÃO foi encontrado na classe!")
        
        parsed_args, unknown = parser.parse_known_args(cli_args)
        print(f"[DEBUG] Parsed args: {vars(parsed_args)}")
        print(f"[DEBUG] Unknown args: {unknown}")
        
        sig = inspect.signature(processor_class.__init__)
        kwargs = {k: v for k, v in vars(parsed_args).items() if k in sig.parameters and v is not None}
        print(f"[DEBUG] Kwargs finais para o init: {kwargs}")

        processor = processor_class(**kwargs)
        json_data = processor.process()

        output_file = OUTPUT_DIR / f"{processor_name}.json"

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4, ensure_ascii=False)

        print(f"Processed successfully: {processor_name}")

    except Exception as e:
        print(f"Failed to process '{processor_name}': {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--processor", type=str)
    args, remaining_args = parser.parse_known_args()

    print(f"[DEBUG] Main - Args: {args}")
    print(f"[DEBUG] Main - Remaining Args (após o --): {remaining_args}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.processor:
        run_processor(args.processor, remaining_args)
    else:
        for file_path in PROCESSORS_DIR.glob("*.py"):
            if file_path.name.startswith("_") or file_path.name.startswith("base_"):
                continue
            run_processor(file_path.stem, remaining_args)

if __name__ == "__main__":
    main()