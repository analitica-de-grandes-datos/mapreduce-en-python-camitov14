#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin.readlines():
        for column in line:
            column=[x.split(",") for x in column]
            column=[x[3] for x in column]
            for word in column:
                sys.stdout.write("{}\t1\n".format(word))

