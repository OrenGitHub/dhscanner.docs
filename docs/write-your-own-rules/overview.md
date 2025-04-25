# Atoms

Code facts are represented by *predicates* and *varaibles*.
For the most part, variables are just *code locations*. Start line, start column, end line and end column.
In addition, the filename itself is also a part of the variable name. Note that special characters inside
the filename are "escaped" ( `/` for instance ).

Here is an exmaple of a simple unary predicate: `kb_callable`.
The example demonstrates that the code "entity" in `pkg/ratelimit/result_test.go` is callbale. That is, a method,
function or lambda.

Atom predicates are prefixed with *kb* for knowledge base.

!!! example "Example"
    ```prolog
    %
    % this is how a code fact looks
    %
    kb_callable( startloc_47_17_endloc_47_21_pkg_slash_ratelimit_slash_result_test_dot_go ).
    ```

The variables' order aims to be understood from context.
Here are the API predicates related to calls:  

!!! info "Calls"
    ```prolog
    kb_arg_i_for_call( Arg, Index, Call ).
    ```

Predicates that are *not* related to the actual code base,
are prefixed with `utils_`, and they are considered to be an integral part of the API:

!!! info "Predicate: utils_arg_for_call / 2"
    ```prolog
    % This is the actual implementation in the code
    utils_arg_for_call( Arg, Call ).
    ```
