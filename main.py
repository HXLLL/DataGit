import sys

def main():
    argc = len(sys.argv)
    print("%d args" % argc)
    for s in sys.argv:
        print(s)

if __name__ == "__main__":
    main()
