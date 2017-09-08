# CLion freeze dump parser

Automatically detect issue IDs related to a CLion freeze.

## Usage

```
./clion-freeze-parser dump.txt > result.txt
```

### Prerequisites

Python 3


### Output

- Notifies if there any `cidr`-related stack frames in the EDT stack at all
- Reports the URLs of the found issues
- Prints the EDT stack trace, with interesting frames marked with `*`

## TODO

- More issue IDs (patches are welcome)
- Configure output (i.e. don't print stack traces by default?)
- Folder processing; `threadDump-*.txt` files grouping
- zip archives processing
