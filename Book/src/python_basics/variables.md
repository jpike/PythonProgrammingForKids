# Variables

- [Memory and Variables Slides](https://docs.google.com/presentation/d/10MAcEF8Y_lPuy_tAfU66H5x-5fc9Zmred88mUElxpMs/)

There are a few important things to remember about variable names in Python:
- Variables names can only include the following characters: letters, numbers, and underscores.
    A number cannot be the first character in a variable name.  Variable names cannot
    contain spaces, but underscores or different capitalization are often used to
    provide visual separation for different words that may be part of a variable name
    (for example, `my_name` or `MyName`).  See <https://docs.python.org/3/reference/lexical_analysis.html#identifiers>
    for more details on variable names.
- Variable names are _case-sensitive_.  This means that variable names with letters
    in different _cases_ (uppercase or lowercase) refer to different variables.
    For example, `variable_name` and `Variable_Name` refer to two different variables.
    Therefore, it's important to make sure you use consistent letter casing when
    you want to reference the same variable.
- If you try to use a variable that hasn't been defined (created) yet, you'll likely
    get an error message that says something like `name 'variable_name' is not defined`.
    This is Python's way of saying it doesn't understand the words you're using for
    a particular variable name because you haven't defined that variable yet to tell
    Python what it is.  A common cause for these kinds of errors is small typos or
    spelling errors in variable names, so check each character in your variable names
    carefully to make sure you're spelling them correctly.
