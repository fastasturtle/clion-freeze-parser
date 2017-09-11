# CLion freeze dump parser

Automatically detect issue IDs related to a CLion freeze.

## Usage

```
./cidr_freeze_parser.py dump.txt > result.txt
```

### Prerequisites

Python 3


### Output

- Reports the URLs of the possibly found issues
- Prints the EDT stack trace, with interesting frames marked with `*`

## TODO

- More issue IDs (patches are welcome)
- Configure output (i.e. don't print stack traces by default?)
- Folder processing; `threadDump-*.txt` files grouping
- zip archives processing
- handle cases where EDT is waiting (e.g. on a read/write lock)