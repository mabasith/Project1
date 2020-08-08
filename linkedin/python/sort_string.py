#!/usr/bin/env python3

def sort_words(input):
    words = input.split()
    
    words = [w.lower() + w for w in words]
    
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

def main():
    print (sort_words("have you Done"))

if __name__=="__main__":
    main()