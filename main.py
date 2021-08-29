from game_files.GUI import *
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            FirstMessage()
        elif len(sys.argv) == 2:
            num_of_cols = int(sys.argv[1])
            FirstMessage(cols=num_of_cols)
        elif len(sys.argv) == 3:
            num_of_cols = int(sys.argv[1])
            gamma = float(sys.argv[2])
            FirstMessage(cols=num_of_cols, gamma=gamma)
        elif len(sys.argv) == 4:
            num_of_cols = int(sys.argv[1])
            gamma = float(sys.argv[2])
            ab_depth = int(sys.argv[3])
            if ab_depth < 1 or ab_depth > 7:
                print("AlphaBeta depth should be an integer between 1 and 7", file=sys.stderr)
                raise Exception
            FirstMessage(cols=num_of_cols, gamma=gamma, ab_depth=ab_depth)
        elif len(sys.argv) == 5:
            num_of_cols = int(sys.argv[1])
            gamma = float(sys.argv[2])
            ab_depth = int(sys.argv[3])
            if ab_depth < 1 or ab_depth > 7:
                print("AlphaBeta depth should be an integer between 1 and 7", file=sys.stderr)
                raise Exception
            exp_depth = int(sys.argv[4])
            if exp_depth < 1 or exp_depth > 2:
                print("Expectimax depth should be an integer between 1 and 2", file=sys.stderr)
                raise Exception
            FirstMessage(cols=num_of_cols, gamma=gamma, ab_depth=ab_depth, exp_depth=exp_depth)
        else:
            print("Too many arguments given, only 4 should be given", file=sys.stderr)
            raise Exception

    except Exception as ex:
        print(
            "ERROR: Invalid program arguments\nExample: \"python main.py <num of columns: "
            "integer which is 7 and above> <gamma:number between 0 and 1> "
            "<AlphaBeta depth: integer between 1 and 7> <Expectimax depth: integer between 1 and 2>\"", file=sys.stderr)
