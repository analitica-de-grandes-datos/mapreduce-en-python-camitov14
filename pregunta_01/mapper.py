#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    data=sys.stdin
    line=[x.split(",") for x in data]
    column=[x[3] for x in line]
    for word in column:
            sys.stdout.write("{}\t1\n".format(word))

