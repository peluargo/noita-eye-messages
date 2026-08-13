# Noita Eye Messages Processor

A modular Python utility to process and decode Noita eye message data into structured JSON files.

## Project Structure

```text
noita-eye-messages/
│
├── input/                             # Raw input data and mappings
│   ├── __init__.py                    # Centralized package imports
│   └── ...
│
├── processors/                        # Data processors
│   ├── base_processor.py              # Abstract base class interface
│   └── messages_as_gun_names.py       # Example of processor implementation
│   └── ...                            # Other implementations
│
├── output/                            # Generated JSON outputs
│   └── messages_as_gun_names.json     # Example of generated output
│   └── ...                            # Other outputs
│
├── main.py                            # Orchestrator script
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

### Running a Specific Processor

You can execute a single processor by passing its name with the `-p` or `--processor` flag:

```bash
python3 main.py -p messages_as_x_letter_from_gun_names

```

### Passing Custom Processor Parameters

Some processors accept custom arguments. To pass parameters to a specific processor, use the `--` separator followed by the custom flags:

```bash
python3 main.py -p messages_as_x_letter_from_gun_names -- -li 3 -fc " " -ps

```

*Note: Command-line parameters can only be passed when executing a specific processor. If no processor is specified, all processors will run using their default values.*

## Processors and Their Parameters

The current project structure supports custom parameters in the processor dedicated to extracting letters from gun names:

### 1. `messages_as_gun_names`

None.

### 2. `messages_as_x_letter_from_gun_names`

This processor extracts specific characters from a list of gun names (`gun_names`) using numeric indices and dynamic alignment.

| Short Flag | Long Flag | Type / Action | Default Value | Description |
| --- | --- | --- | --- | --- |
| `-li` | `--letter_index` | `int` | `0` | Index of the character to be extracted from each gun name. |
| `-fc` | `--fallback_character` | `str` | `" "` | Character used if the index exceeds the gun name length. |
| `-ps` | `--pad_start` | `action="store_true"` | `False` | Pads missing spaces at the start (right-align) instead of the end to equalize string lengths. |

---

*Note: Other processors in the directory that do not implement the `add_args` method will run normally using their default internal values, ignoring any extra arguments provided after the `--` separator.*