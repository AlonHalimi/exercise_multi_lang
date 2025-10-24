#!/usr/bin/env python3
"""
Hello2 World Project 2
Another Python program that prints "hello2 world" with additional features
"""

import sys
from datetime import datetime

def print_hello2_world():
    """Function that prints hello2 world with timestamp"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] hello2 world")

def main():
    """Main function"""
    print_hello2_world()
    print("This is hello2 world project 2!")

if __name__ == "__main__":
    main()

