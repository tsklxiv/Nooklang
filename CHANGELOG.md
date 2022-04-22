# Changelog

## 0.1 (14/10/2021)

Initial version.

## 0.2 (14/10/2021)

Add the 'd' (short for 'duplication') operator.

## 0.3 (14/10/2021)

Seperate from symbol and identifier, so now '+' are different from 'add'.

## 0.4 (14/10/2021)

Change the store/load operators. Now, to store value to a variable, do `s<VAR_NAME>`
instead of `{<VAR_NAME>}s`.

The same as load variable: `l<VAR_NAME>`.

## 0.5 (15/10/2021)

Add logical operators:

- `>`  (Less than)
- `<`  (Greater than)
- `>=` (Less or equal)
- `<=` (Greater or equal)
- `<>` (Not equal)
- `~`  (Not)
- `&`  (And)
- `|`  (Or)

Examples:

```
50 50 = w # 50 == 50
40 50 < w # 50 < 40
50 50 <> 20 20 = | w # 50 != 50 or 20 == 20
```

You can also see the `logical_op` example in `examples/`.

## 0.6 (15/10/2021)

Add the `?` operator.

`?` is basically the `if` function.

Format of `?`:

```
{<if>}{<then>}{<else>}?
```

You can also see the `if` example in `examples/`.

## 0.6.1 (15/10/2021)

- Change the `logical_op` example (`examples/logical_op.nook`)

## 0.7 (15/10/2021)

- Add the `t` operator.

`t` is short for `trap` and it is used as a while loop.

Format of `t`:

```
{<condition>}{<block>}l
```

Note that if `condition` is an empty string, that means a infinite loop.

You can also see the `truth_machine` example in `examples/`.

- Fix the string consume when the string is empty

## 0.7.1 (15/10/2021)

- Change how the `t` command works, now it just a infinite loop command.

## 0.7.2 (02/03/2022)

Sorry for such a long time not updating this.

- Add
	- `b` (convert int to binary string)
	- `l` (length of string)
	- `c` (count the number of appearance of a substring in string)

## 0.7.3 (15/03/2022)

- Remove all the operators added in `0.7.2`, as they are not proved to be very useful by the author.
- Fix the while loop

## 0.7.4 (22/04/2022)

- Add operator `c`: Converts number to character
