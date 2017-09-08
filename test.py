import glob
import os

from cidr_freeze_parser import process_thread_dump


def run_tests():
    for fileName in glob.iglob("testdata/*.txt"):
        gold_name = fileName + ".gold"
        out_name = fileName + ".out"
        try:
            os.remove(out_name)
        except FileNotFoundError:
            pass

        with open(fileName) as inputFile, open(gold_name) as goldFile:
            result = process_thread_dump(inputFile.readlines())
            gold = goldFile.readlines()
            if "".join(result).strip() != "".join(gold).strip():
                with open(out_name, "w") as outFile:
                    outFile.writelines(result)
                print(fileName + " failed")


if __name__ == '__main__':
    run_tests()
