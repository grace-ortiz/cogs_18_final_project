from my_module.functions import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--misses', type=int)
parser.add_argument('--ships', type=int)
parser.add_argument('--both', type=int, nargs=2)
args = parser.parse_args()

if args.misses:
    play_game(allowed_misses=args.misses)
elif args.ships:
    play_game(n_ships=args.ships)
elif args.both:
    play_game(allowed_misses=args.both[0], n_ships=args.both[1])
else:
    play_game()