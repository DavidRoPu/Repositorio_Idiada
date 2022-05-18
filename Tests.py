# Coding Problem Tests of FUNCTIONS
# David Romero Puyal
# davidrompuy99@gmail.com
# 679034125



#Read file prove
with open('data', "r") as fdname:
        nrov = len(fdname.readlines())
        # print(nrov, '\n')
with open('data', "r") as fdname:
        i = 0
        while i < nrov:
                # print(fdname.readline())
                i+=1



#Write file prove
with open('solution', "w") as fsname:
        fsname.write('OUTPUT\n')
with open('data', "r") as fdname:
    nrov = len(fdname.readlines())
    i = 0
    while i < nrov:
        with open('solution', "a") as fsname:
                # fsname.write("%i\n" % (i))
                i+=1




# FUNCTIONS

# Rotating left function.
def rotate_left(ori):
    if ori == 'N':
        return 'W'
    elif ori == 'W':
        return 'S'
    elif ori == 'S':
        return 'E'
    elif ori == 'E':
        return 'N'

# Rotating Right function.
def rotate_right(ori):
    if ori == 'N':
        return 'E'
    elif ori == 'W':
        return 'N'
    elif ori == 'S':
        return 'W'
    elif ori == 'E':
        return 'S'

# Advance 1 square function.
def move(x, y, ori, ymax, xmax, ymin, xmin):
    if ori == 'N':
        y += 1
        if y > ymax:
            y = 'X'
    elif ori == 'E':
        x += 1
        if x > xmax:
            x = 'X'
    elif ori == 'S':
        y -= 1
        if y < ymin:
            y = 'X'
    elif ori == 'W':
        x -= 1
        if x < xmin:
            x = 'X'
    return x, y



#FUNCTIONS TESTS

# Right rotation test
def test_rotate_right(ori, ori_expected):
    try:
        assert rotate_right(ori) == ori_expected
        print ("Test Rotate Right OK")
    except:
        print("Test Rotate Right Wrong")

# Left rotation test
def test_rotate_left(ori, ori_expected):
    try:
        assert rotate_left(ori) == ori_expected
        print ("Test Rotate Left OK")
    except:
        print("Test Rotate Left Wrong")

# Move test functions
def test_move(x, y, ori, ymax, xmax, ymin, xmin, resultx, resulty):
    try:
        assert move(x, y, ori, ymax, xmax, ymin, xmin) == (resultx, resulty)
        print ("Test Move OK")
    except:
        print("Test Move Wrong")


if __name__ == "__main__":

    #Expected OK Tests
    print ("EXPECTED OK TESTS")
    test_rotate_right('N', 'E')
    test_rotate_left('N', 'W')
    test_move(1, 2, 'N', 5, 5, 0, 0, 1, 3)
    print('\n')

    # Expected WRONG Tests
    print("EXPECTED WRONG TESTS")
    test_rotate_right('N', 'W')
    test_rotate_left('N', 'E')
    test_move(1, 2, 'N', 5, 5, 0, 0, 1, 5)
    test_move('N', 1, 2, 5, 5, 0, 0, 1, 5)