# llm-verifier

a repo that runs lint, type checking, and tests on llm generated code

## usage

each subdirectory is configured to verify some particular tech stack.

place your llm-generated code in the `main` file, e.g. `main.py` or `main.ts`

then, place unit tests in the `main_test` file.

then, run unit tests and linting.

for JS and TS this is `npm run test` and `npm run lint`

for other languages, see the README.md file within the directory.
