#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        for column in line.split(","):
            for word in column[3]:
                sys.stdout.write("{}\t1\n".format(word))
