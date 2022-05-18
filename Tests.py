#Tests for read file

with open('data', "r") as fdname:
        nrov = len(fdname.readlines())
        print(nrov, '\n')

with open('data', "r") as fdname:
        i = 0
        while i < nrov:
                print(fdname.readline())
                i+=1



#Tests for write file

with open('solution', "w") as fsname:
        fsname.write('OUTPUT\n')

with open('data', "r") as fdname:
    nrov = len(fdname.readlines())
    i = 0
    while i < nrov:
        with open('solution', "a") as fsname:
                fsname.write("%i\n" % (i))
                i+=1


