# CI/CD

Scanning your code on every pull request is the preferred way
of monitoring your applications for vulnerabilities. Your code never
leaves the workflow environment. It is not logged anywhere.
There are no incremental scans, and no part of your code is cached.
The rules used to scan your code were carefully picked by both
LLMs and security professionals. Normal users don't need to adjust
rules at all ( though they sure *can* if they want to ).

!!! note "Note"
    Currently, only GitHub Action yaml is supported.
    Jenkins, CircleCI and others will be released soon

Simply copy this yaml to your GitHub actions:

??? info "GitHub Action ( *click to watch* )"
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