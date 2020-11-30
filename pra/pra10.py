# -----------------------------------
# Lecture 19 and practical 10
# --------------------------------

a = [8,4,1,5,2,6,3,7,9,10]
def bubble_sort(a):
    swapped = True
    number_of_iteration = 0
    while swapped:
        swapped = False
        for i in range(len(a)-1):
            n1 = a[i]
            n2 = a[i+1]
            if n1>n2:
                a[i:i+2] = [n2,n1]
                swapped = True
        number_of_iteration += 1
    print("Bubble sort completed in ",number_of_iteration," times.")
    return a

def bubble_sort2(a):
    swap = len(a)-1
    if swap > 1:
        do_it = False
        for h in range(swap):
            for i in range(swap):
                while a[i]>a[i+1]:
                    c = a[i]
                    a[i] = a[i+1]
                    a[i+1] = c
            # print(a)
            swap -= 1
            # print(swap)
    return a

print(bubble_sort2(a))


def apart(a):
    x=[]
    y=[]
    for i in range(len(a)//2):
        x.append(a[i])
    for h in range(len(a)//2,len(a)):
        y.append(h)

    return [x,y]

# def merge_sort(a):
    # lenx = len(a[0])
    # if lenx == 1:
    #     return
    # return apart(a)

# merge_sort(a)
