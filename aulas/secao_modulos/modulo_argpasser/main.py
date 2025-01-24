from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b')
args = parser.parse_args()
print(args.b)