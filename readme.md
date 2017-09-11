# CLion freeze dump parser

Automatically detect issue IDs related to a CLion freeze.

## Usage

```
./cidr_freeze_parser.py 'freezeFolder/**/*.txt > result.txt
```

### Prerequisites

Python 3


### Output

- Prints a summary of the possibly found issues
- Prints a file:issue mapping
- Prints the EDT stack trace for unrecognized traces 

## TODO

- More issue IDs (patches are welcome)
- `threadDump-*.txt` files grouping
- zip archives processing
- handle cases where EDT is waiting (e.g. on a read/write lock)