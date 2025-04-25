# Scanning at scale

Are you trying to find malicious code at scale ? We like you already !

!!! note "Note"
    Check the [queries][1] used for our CI/CD scanner. It's a great place to start.

Let's write a simple query for counting minified functions.
Don't worry if you're not a Prolog expert. You don't have to be.
If you ever played Lego when you were a kid - you should be fine.

!!! tip "Pro Tip"
    Use *any* LLM you like to build Prolog queries from Dhscanner atoms

Dhscanner accepts its queries as part of the `tar`-ed repo in a special
`Prolog` file called `.dhscanner.queries`. It is shown below as a one-liner,
but clearly, you can edit this file and paste the results of your vibe-coding
session in a more readable format. Remember, you don't have to be a Prolog expert
to write queries. Literally *any* ( untrained ) LLM will be happy to translate your English specification
to a proper Prolog file. Now fasten your seat belt and let's launch our query:

```bash
$ cd to/the/repo/you/want/to/scan
$ echo "minified(N) :- findall(C,(kb_callable(C),kb_has_fqn(C,Fqn),string_length(Fqn,Len),Len =< 2), L),length(L, N)." > .dhscanner.queries
$ tar -cz . | curl -X POST -H "X-Code-Sent-To-External-Server: false" -H "Content-Type: application/octet-stream" -H "X-Ignore-Testing-Code: true" --data-binary @- http://127.0.0.1:8000/
```

[1]: https://github.com/OrenGitHub/dhscanner.query.engine/blob/main/utils.pl