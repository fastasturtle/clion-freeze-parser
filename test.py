import glob
import os
import sys

from cidr_freeze_parser import process_files


def run_tests():
    overwrite = len(sys.argv) > 1 and sys.argv[1] == "--overwrite"
    for file_name in glob.iglob("testdata/*.txt"):
        gold_name = file_name + ".gold"
        out_name = file_name + ".out"
        try:
            os.remove(out_name)
        except FileNotFoundError:
            pass

        with open(gold_name) as gold_file:
            result = process_files(file_name)
            gold = gold_file.readlines()
            if "".join(result).strip() != "".join(gold).strip():
                with open(out_name, "w") as out_file:
                    out_file.writelines(result)
                print(file_name + " failed")

                if overwrite:
                    print("Overwriting...")
                    os.rename(out_name, gold_name)




if __name__ == '__main__':
    run_tests()
