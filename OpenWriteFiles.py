my_list = ('1', '2', '340')
#w+ will write to a new file
#a+ will append to a new file
#a will append a file

testfileit=open("testfile.txt", "a+")
start_file = testfileit.write('Distance between Psap and all sites')
testfileit.write("\n"*2)
testfileit.close()


#How to iterate a line of text to a file x times.
appenfile = open("testfile.txt", "a")
blah = ("be amazed dude")
for x in range(10):
    appenfile.write(blah)
    appenfile.write("\n")
appenfile.close()
