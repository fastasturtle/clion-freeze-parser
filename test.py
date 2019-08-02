import os
import sys

from cidr_freeze_parser import parse_args_and_process_files


def run_tests():
    overwrite = len(sys.argv) > 1 and sys.argv[1] == "--overwrite"
    for f in os.listdir('testdata'):
        if f.endswith('.gold') or f.endswith('.out'):
            continue

        file_name = 'testdata/' + f
        gold_name = file_name + ".gold"
        out_name = file_name + ".out"

        if os.path.exists(out_name):
            os.remove(out_name)

        with open(gold_name) as gold_file:
            result = parse_args_and_process_files([file_name])
            gold = gold_file.readlines()
            if "".join(result).strip() != prepare_gold(gold):
                with open(out_name, "w") as out_file:
                    out_file.writelines(result)
                print(f + " failed")

                if overwrite:
                    print("Overwriting...")
                    os.rename(out_name, gold_name)


def prepare_gold(gold):
    return "".join(filter(lambda g: g != "\n", gold)).strip()


if __name__ == '__main__':
    run_tests()
