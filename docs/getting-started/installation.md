# CLI

Running dhscanner locally is easy - You just need docker:
```bash
$ git clone --recurse-submodules https://github.com/OrenGitHub/dhscanner
$ cd dhscanner
$ docker compose -f compose.rel.x64.yaml up -d
```
To test your code:
```bash
$ cd to/the/repo/you/want/to/scan
$ tar -cz . | curl -v -X POST -H "X-Code-Sent-To-External-Server: false" -H "Content-Type: application/octet-stream" --data-binary @- http://127.0.0.1:443/ > output.sarif
```