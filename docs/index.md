# Home

Dhscanner is a highly-parallel static code analyzer ( [SAST][1] engine ).
It aims to compete with established solutions like [Semgrep][2],
[Opengrep][3] and [CodeQl][5], while being **completely free** for both
public and **private** repositories. The feauture that allows it to
discriminate false positive findings is its ability to sematically understand
**user-input sanitation**. This feature enabled us to achieve a significantly low
false alarms ratio compared to other SAST solutions. 

!!! info "Info"
    Dhscanner was built as a collaborative research
    effort by a team of programming languages Phd's from [Tel Aviv University][6].

There are three ways to use dhscanner:

- From [CI/CD pipelines](getting_started/ci_cd.md) ( 👈 preferred and easiest way )
- From the [CLI](getting_started/cli.md)
- Use our "monstrous" server ( mostly for research )

!!! info "Info"
    It is possible to shift your non-research workload to our server.
    Please [open up an issue][7] if this is relevant for your needs.

[1]: https://en.wikipedia.org/wiki/Static_application_security_testing
[2]: https://semgrep.dev/index.html
[3]: https://www.opengrep.dev/
[4]: https://docs.github.com/en/get-started/learning-about-github/about-github-advanced-security
[5]: https://codeql.github.com/
[6]: https://english.tau.ac.il/
[7]: https://github.com/OrenGitHub/dhscanner/issues