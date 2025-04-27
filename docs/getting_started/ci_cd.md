# CI/CD

!!! info "Info"
    The **easiest** way to monitor your application is
    by setting a regular workflow to scan your code on
    every **push** and **pull request**. Even for code repositories with
    thousands of files, it typically takes just a couple of minutes
    to complete.

We care about your privacy. Your code never
leaves the workflow environment. It is not logged anywhere.
There are no incremental scans. No part of your code is cached.

!!! tip "Pro Tip"
    Normal users don't need to configure **anything**.
    The default setting of our scanner uses rules that were **carefully picked** by both
    security professionals and large language models ( LLMs ).

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