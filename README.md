# Noita Eye Messages Processor

A modular Python utility to process and decode Noita eye message data into structured JSON files.

## Project Structure

```text
noita-eye-messages/
│
├── input/                           # Raw input data and mappings
│   ├── __init__.py                  # Centralized package imports
│   └── ...
│
├── processors/                      # Data processors
│   ├── base_processor.py            # Abstract base class interface
│   └── messages_as_gun_names.py     # Example of processor implementation
│   └── ...                          # Other implementations
│
├── output/                          # Generated JSON outputs
│   └── messages_as_gun_names.json   # Example of generated output
│   └── ...                          # Other outputs
│
├── main.py                          # Orchestrator script
├── .gitignore
└── README.md
```

## Generating outputs

All the outputs are generated at once by the `main.py` file call. Every `BaseProcessor` file will be automatically called and executed when running the project.

## Running the project

Run the following command at the project root:

```bash
python3 main.py
```