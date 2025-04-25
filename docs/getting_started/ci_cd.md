# CI/CD

Scan your code on every push / pull request - it's that fast.
Your code never leaves the workflow. It is not logged anywhere.
We don't even have a database 😉. There are no incremental scans,
we care about your privacy, and don't cache *any* part of your code.

!!! note "Note"
    Currently, only GitHub Actions yaml flavor is supported.
    Please open an issue if you are using other pipelines.

Simply copy this to your GitHub actions:

```yaml
name: dhscanner-sast

on:
  push:
    branches:
      - main

jobs:
  run-dhscanner:
    runs-on: ubuntu-latest

    steps:
      - name: clone dhscanner (with submodules)
        run: |
          git clone --recurse-submodules https://github.com/OrenGitHub/dhscanner
          cd dhscanner
          docker compose -f compose.rel.x64.yaml up -d

      - name: checkout specific tag
        uses: actions/checkout@v4

      - name: send the whole repo to dhscanner
        run: |
          tar -cz . | curl -v -X POST \
            -H "X-Code-Sent-To-External-Server: false" \
            -H "Content-Type: application/octet-stream" \
            --data-binary @- http://127.0.0.1:443/ > output.sarif

      - name: Upload SARIF results
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: output.sarif

      - name: fail workflow if sarif contains findings
        run: |
          if jq '.runs[].results | length > 0' output.sarif | grep -q 'true'; then
            echo "Sarif findings detected, failing the workflow"
            exit 1
          fi
```