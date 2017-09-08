# CLion freeze dump parser

Automatically detect issue IDs related to a CLion freeze.

## Usage

```
./clion-freeze-parser dump.txt > result.txt
```

### Prerequisites

Python 3


### Output

Notifies if there any `cidr`-related stack frames in the EDT stack at all,
reports the URLs of the found issues, and prints the EDT stack trace, with
interesting frames marked with `*`.

## TODO

- More issue IDs (patches are welcome)
- Folder processing; `threadDump-*.txt` files grouping
- zip archives processing
