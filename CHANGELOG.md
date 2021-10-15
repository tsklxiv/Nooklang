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
