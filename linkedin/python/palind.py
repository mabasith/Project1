#!/usr/bin/env python3

import re
def is_palindrome(phrase):
    forward = ''.join(re.findall(r'[a-z]+', phrase.lower()))
   
    backwards = forward[::-1]
    
    return forward == backwards

def main():
   print(is_palindrome("Go hang a salami, I'm a lasagna hog.")) 

if __name__ == "__main__":
    main()
