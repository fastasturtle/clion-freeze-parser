# CLion freeze dump parser

Automatically detect issue IDs related to a CLion freeze.

## Usage

```
./cidr_freeze_parser.py 'freezeFolder/**/*.txt > result.txt
./cidr_freeze_parser.py freezeFolder > result.txt
./cidr_freeze_parser.py dump.txt > result.txt
```

### Prerequisites

Python 3


### Output

- prints a summary of the possibly found issues
- prints a file:issue mapping
- prints the EDT stack trace for unrecognized traces 

## TODO

- more issue IDs (patches are welcome)
- better error handling
- `threadDump-*.txt` files grouping
- extract wait duration from the folder name
- zip archives processing
- handle cases where EDT is waiting (e.g. on a read/write lock); report non-waiting traces with it
- have a persistent DB of processed traces