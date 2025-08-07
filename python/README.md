# llm-verifier/python

this subdirectory uses uv for package management and virtual environment control

first, install and run the app harness using [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv
source .venv/bin/activate
# or, `source .venv/Scripts/activate` on Windows
uv pip install -r pyproject.toml
```

we use mypy, ruff, and pytest for type checking, linting, and test running.

you can now run the example file validations:

```bash
uv run pytest main_test_example.py
uv run mypy main_example.py
uv run ruff check main_example.py
```

target your local files without the example substring in the file name to similarly review them.
in many cases you will need to temporarily install third party libraries to get the code to run or pass checks. That's smart to do locally! These script-specific changes should not be contributed to the upstream repo.
