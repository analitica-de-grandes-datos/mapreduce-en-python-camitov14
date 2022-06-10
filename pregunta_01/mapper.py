#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        line = [x.split("\t") for x in line]
        for column in line:
            column=[x.split(",") for x in column]
            for word in column[3]:
                sys.stdout.write("{}\t1\n".format(word))
