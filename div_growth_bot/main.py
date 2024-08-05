#!/usr/bin/env python3

import argparse
from logic import logic
from web import web

def main():
    parser = argparse.ArgumentParser(description="Stock Trading Bot")
    parser.add_argument('--web', action='store_true', help="Display results on a website")
    args = parser.parse_args()

    if args.web:
        web.display_website()
    else:
        logic.print_results()

if __name__ == "__main__":
    main()
