# rpn

A simple reverse polish notation (RPN) calculator

# Quick Start

This is a Python 3 program so run with either:

```
python3 rpn.py
```

or just:

```
python rpn.py
```

At the `RPN>` prompt type:

```
2
```

then type:

```
2
```

again and then type:

```
+
```

and you get your answer.

Here are the operatorss the `RPN` program uses:

```
+ for addition
- for subtraction
* for multiplication
/ for division
```

Remember to type the operands first and the operator second.  That is what Reverse
Polish Notation is all about.

More info on Reverse Polish notation here:

[Wikipedia entry for Reverse Polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)

# A stack based calculator

The `RPN` program is stack based.  When you type a number it is placed on stack.
When you type an operator like `+` the two items on top of the stack are removed from
the stack, added together and the result placed back on the stack.  The result is
also printed.

If there are not enough numbers on the stack and you type an operator you
will get an error message similar to:

```
<too few items on stack>
```

# Special commands

There are a few special commands that the `RPN` program understands.

Typing `exit` will make the `RPN` program finish.

Typing `drop` will remove the number currently on top of the stack.  This is useful
if the last number you entered was incorrect.

Typing `.` (the period/full stop character) will print the number currently
on the top of the stack.

Typing `dropall` will remove all the numbers from the stack.  

Typing `..` (two period/full stop characters) will print all the numbers currently
on the stack.  The most recently added number (i.e. the number on top of the stack) is
printed first.

# The rpn.bat file

If you are on a Windows machine you might want to copy the `rpn.bat` file
to a directory in your `PATH` environment variable such
as `C:\Windows`.  You may need administrator priviledges to do this.

Once `rpn.bat` is in a directory on your `PATH` you should be able
to run it from the  Windows search box by just typing `rpn`.  On
Windows 10 select the option:

```
rpn
Run Command
```

# Why not use the Windows Calculator?

If you have a Windows calculator installed then use that - it will have
all the features you need.

However, I just wanted something to add, subtract, multiply and divide numbers.

Also, I like coding and, for me, that was reason enough :-]

-------------------------------------

End of README.md
