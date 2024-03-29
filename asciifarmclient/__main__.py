

import sys

if sys.version_info[0] < 3:
    print("This game is written in python 3.\nRun 'python3 "+sys.argv[0]+"'")
    sys.exit(-1)

if __package__ == "asciifarmclient":
    from . import main
else:
    import os.path
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from asciifarmclient import main

main.main()
