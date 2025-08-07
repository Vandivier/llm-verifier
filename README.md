# llm-verifier

a repo that runs quality checks on standalone llm-generated scripts.

currently we support lint, type checking, and unit tests on llm generated code

contributions are welcome for automated security scanning, integration testing, semantic review, and other forms of static analysis.

these scans are currently designed to ignore formatting. we assume any code consumer will have an opionated formatter, so we stick to other checks.

## usage

each subdirectory is configured to verify some particular tech stack.

place your llm-generated code in the `main` file, e.g. `main.py` or `main.ts`

then, place unit tests in the `main_test` file.

these files will be ignored by git. There are example files for reference as well, like `main_example.py` and so on.

with your real code to test and the related tests, now run unit tests and linting:

1. for JS and TS this is `npm run test` and `npm run lint`
2. for other languages, see the README.md file within the directory.
