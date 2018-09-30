# CLion freeze dump parser

Automatically detects issue IDs related to a CLion freeze.

## Usage

```
python ./cidr_freeze_parser.py dump.txt
python ./cidr_freeze_parser.py freezeFolder
```

If a folder name has a `threadDumps-freeze-20` substring, all containing dumps
are assumed to have a single cause (and only one is processed).

Results are stored in `out` directory.    

### Output

- prints a summary of the possibly found issues
- prints a file:issue mapping
- prints the EDT stack trace for unrecognized traces 

## TODO

- more issue IDs (patches are welcome)
- better error handling
- extract wait duration from the folder name
- zip archives processing
- handle cases where EDT is waiting (e.g. on a read/write lock); report non-waiting traces with it
- have a persistent DB of processed traces
- Refactor the code to use a single generator that pipes straight to the analyzer
(so if a file from a `theadDump` folder fail to parse), we can take a next one instead.