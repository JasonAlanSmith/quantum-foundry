# Quantum Foundry

Quantum Foundry is a schema-aware test data generation tool designed
for engineers, QA professionals, and developers who need structured,
reproducible data for relational databases.

It inspects existing schemas, suggests generation strategies, and emits
SQL scripts using deterministic random generation.

------------------------------------------------------------------------

## Project Status

**Quantum Foundry is in early development.**

Version `v0.1.0` is a proof-of-concept release that validates the core workflow:

- Project initialization
- Configuration-driven schema inspection
- Strategy suggestion
- Deterministic data generation
- SQL emission via CLI

At this stage:

- Generated values are intentionally simple (e.g., placeholder text patterns and small randomized sets).
- Type coverage is limited.
- Realistic domain-aware data generation is still evolving.
- Breaking changes should be expected as the architecture matures.

This release exists to:

- Establish a stable CLI and packaging foundation.
- Validate the inspect → plan → generate → emit pipeline.
- Enable incremental improvement of planners and generators.
- Provide a public artifact for feedback and iteration.

Quantum Foundry is not yet intended for production data generation workflows. Future releases will expand planner sophistication, improve realism, and strengthen architectural boundaries.

## Features

- Inspect relational database schemas
- Suggest generation strategies based on column types and patterns
- Deterministic random data generation (seed-based)
- SQL `INSERT` script emission
- CLI-first design
- Extensible architecture (planners, suggestors, emitters)
- Structured logging with UTC timestamps

------------------------------------------------------------------------

## Requirements

- Python 3.14+

------------------------------------------------------------------------

## Installation

Install from PyPI (Coming Soon!):

``` bash
pip install qf
```

After installation, the CLI command `qf` will be available.

------------------------------------------------------------------------

## Quick Start

### 1️⃣ Initialize a Project

Create a new Quantum Foundry project:

``` bash
qf project init my_project
```

This creates a project directory containing configuration files.

------------------------------------------------------------------------

### 2️⃣ Configure the Project

Edit the generated configuration file (TOML format) to define:

- Database connection settings
- Target schema
- Generation options
- Output settings

------------------------------------------------------------------------

### 3️⃣ Inspect a Schema

Run schema inspection:

``` bash
qf inspect --config path/to/config.toml
```

Quantum Foundry will:

- Connect to the configured data source
- Inspect tables and columns
- Suggest generation strategies
- Emit SQL scripts according to configuration

------------------------------------------------------------------------

## Example Workflow

``` bash
qf project init demo_project
# edit demo_project/config.toml

qf inspect --config demo_project/config.toml
```

Output SQL scripts can then be executed against your target database.

------------------------------------------------------------------------

## Logging

Quantum Foundry uses structured logging with:

- UTC timestamps
- Verbosity levels (`-v`)
- Optional file logging (`--log-file`)

Example:

``` bash
qf inspect --config config.toml -v --log-file logs/
```

If a directory is provided to `--log-file`, a timestamped log file will
be created automatically.

------------------------------------------------------------------------

## CLI Overview

``` bash
qf --help
qf project --help
qf inspect --help
```

------------------------------------------------------------------------

## Architecture

Quantum Foundry follows a layered design that separates:

- CLI interface
- Application orchestration
- Domain logic (suggestors, planners)
- Infrastructure (inspectors, emitters)

Future releases will further expand this architecture toward a full
DDD/Clean Architecture structure.

------------------------------------------------------------------------

## Development

Clone the repository:

``` bash
git clone 
cd 
```

Create a virtual environment:

``` bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
```

Install development dependencies:

``` bash
pip install -r requirements-dev.txt
```

Run tests:

``` bash
pytest
```

Build locally:

``` bash
python -m build
twine check dist/*
```

------------------------------------------------------------------------

## Contributing

Please see `CONTRIBUTING.md` for contribution guidelines.

All contributors are expected to follow the `CODE_OF_CONDUCT.md`.

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

------------------------------------------------------------------------

## Roadmap

- v0.1.x --- Stabilization and packaging
- v0.2.0 --- DDD/Clean Architecture refactor
- v0.3.x --- Expanded planners and generation strategies

------------------------------------------------------------------------
