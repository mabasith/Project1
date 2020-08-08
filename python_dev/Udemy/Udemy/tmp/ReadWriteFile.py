#if test.txt is not present "w"will create it automatically.
file = open("test.txt","w")
file.write("Sample tex")
file.close()
#appending text use "a"
file = open("test.txt","a")
file.write(" Hai, I am Basith.")
file.close()