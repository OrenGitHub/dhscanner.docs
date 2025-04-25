# Atoms

Code facts are represented by *predicates* and *varaibles*.
For the most part, variables are just *code locations*.
Start line, start column, end line and end column.
In addition, the filename itself is also a part of the variable name.
Note that special characters inside the filename are "escaped" ( `/` for instance ).

!!! example "Example"
    ```prolog
    %
    % this is how a code fact looks like:
    %
    kb_callable( startloc_47_17_endloc_47_21_pkg_slash_ratelimit_slash_result_test_dot_go ).
    ```

Atom predicates are prefixed with *kb* for knowledge base.

!!! info "Strings"
    ```prolog
    kb_const_string( String, 'value' ).
    ```

The variables' order aims to be understood from context.

!!! info "Calls"
    ```prolog
    kb_call( Call ).
    kb_arg_for_call( Arg, Call ).
    kb_arg_i_for_call( Arg, Index, Call ).
    ```

Callables are functions, methods and lambdas.

!!! info "Callables"
    ```prolog
    kb_callable( Callable ).
    kb_callable_has_param( Callable, Param ).
    ```

Class inheritance is of bounded depth. So are *all* transitive closures.

!!! info "Classes"
    ```prolog
    kb_class_name( Class, 'name' ).
    kb_subclass_of( Class, 'super' ).
    kb_method_of_class( Method, Class ).
    ```

Dataflow edges are by far the most common facts.

!!! info "Dataflow"
    ```prolog
    kb_dataflow( From, To ).
    ```
