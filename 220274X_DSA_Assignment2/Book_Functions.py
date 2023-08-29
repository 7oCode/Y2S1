from Books import *
from Customer import *
from tabulate import tabulate
import pandas as pd
from openpyxl.workbook import Workbook


def bubblesort(blist, book_dict):
    for key in book_dict:
        blist.append(book_dict.get(key))

    for i in range(len(blist)-1, 0, -1):
        for j in range(i):
            if blist[j].get_category() > blist[j+1].get_category():
                blist[j], blist[j+1] = blist[j+1], blist[j]
    jlist = []
    for f in blist:
        flist = [f.get_isbn(), f.get_category(), f.get_title(), f.get_publisher(), f.get_year_published()]
        jlist.append(flist)
    table = tabulate(jlist, headers=['ISBN', 'Category', 'Title', 'Publisher', 'Year Published'], tablefmt='grid')
    print(table)


def selection_sort(blist, book_dict):
    for key in book_dict:
        blist.append(book_dict.get(key))

    for i in range(len(blist)-1):
        bigN = i
        for j in range(i+1, len(blist)):
            if blist[j].get_publisher() < blist[bigN].get_publisher():
                bigN = j
        if bigN != i:
            blist[i],blist[bigN] = blist[bigN], blist[i]

    jlist = []
    for f in blist:
        flist = [f.get_isbn(), f.get_category(), f.get_title(), f.get_publisher(), f.get_year_published()]
        jlist.append(flist)
    table = tabulate(jlist, headers=['ISBN', 'Category', 'Title', 'Publisher', 'Year Published'], tablefmt='grid')
    print(table)

def insertion_slot(blist, book_dict):
    for key in book_dict:
        blist.append(book_dict.get(key))

    for i in range(1, len(blist)):
        j = i
        while blist[j-1].get_title() > blist[j].get_title() and j > 0:
            blist[j-1], blist[j] = blist[j], blist[j-1]
            j -= 1

    jlist = []
    for f in blist:
        flist = [f.get_isbn(), f.get_category(), f.get_title(), f.get_publisher(), f.get_year_published()]
        jlist.append(flist)
    table = tabulate(jlist, headers=['ISBN', 'Category', 'Title', 'Publisher', 'Year Published'], tablefmt='grid')
    print(table)


# sort by year then title, ascending
def merge_sort(blist):
    if len(blist) > 1:
        left_side = blist[:len(blist)//2]
        right_side = blist[len(blist)//2:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = 0
        j = 0
        k = 0
        while i < len(left_side) and j < len(right_side):
            if left_side[i].get_year_published() == right_side[j].get_year_published() and (left_side[i].get_isbn() > right_side[i].get_isbn()):
                blist[k] = left_side[i]
                i += 1
            elif left_side[i].get_year_published() > right_side[j].get_year_published():
                blist[k] = left_side[i]
                i += 1
            else:
                blist[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            blist[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            blist[k] = right_side[j]
            j += 1
            k += 1


def show_merge_sort(blist):
    merge_sort(blist)
    jlist = []
    for f in blist:
        flist = [f.get_isbn(), f.get_category(), f.get_title(), f.get_publisher(), f.get_year_published()]
        jlist.append(flist)
    table = tabulate(jlist, headers=['ISBN', 'Category', 'Title', 'Publisher', 'Year Published'], tablefmt='grid')
    print(table)


def display_books(blist, book_dict):
    for key in book_dict:
        blist.append(book_dict.get(key))

    jlist = []
    for f in blist:
        flist = [f.get_isbn(), f.get_category(), f.get_title(), f.get_publisher(), f.get_year_published()]
        jlist.append(flist)
    table = tabulate(jlist, headers=['ISBN', 'Category', 'Title', 'Publisher', 'Year Published'], tablefmt='grid')
    print(table)


def createBook(book_dict):
        try:
            isbn = input("Enter the ISBN (Numbers only): ")
            year_published = input("Enter the year published (Numbers only): ")

            while (isbn.isdigit() and year_published.isdigit()) != True:
                print("Only numbers are allowed")
                if isbn.isdigit() != True:
                    isbn = input("Enter the ISBN (Numbers only): ")
                elif year_published.isdigit() != True:
                    year_published = input("Enter the year published (Numbers only): ")
                else:
                    int(year_published)
                    break

            while not 1800 <= int(year_published) <= 2023:
                print("Books must be from 1800 to 2023")
                year_published = input("Enter the year published (Numbers only): ")
                if year_published.isdigit() and (1800 <= int(year_published) <= 2023):
                    break

            title = input("Enter the title: ").title()
            category = input("Enter the category: ")
            publisher = input("Enter the publisher (Letters only): ")
            schar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}', '[', ']',':',
                     ';', '"', "'", '<', '>', ',', ".", '/', '?']

            # ncheck = True
            # for i in schar:
            #     if category.__contains__(i):
            #         break
            #     else:
            #         ncheck = False


            while (category.isalpha() and publisher.isalpha()) == False:
                if category.isalpha() == False:
                    category = input("Enter the category: ")
                    # for a in schar:
                    #     if category.__contains__(a):
                    #         ncheck = True
                    #         break
                    #     else:
                    #         ncheck = False

                elif publisher.isalpha() == False:
                    print("Only letters are allowed")
                    publisher = input("Enter the publisher (Letters only): ")
                else:
                    break

        except:
            print("Only valid types")

        newbook = Books(isbn, title, category.title(), publisher, year_published)
        book_dict[newbook.get_isbn()] = newbook
        print(f"Book ID {newbook.get_isbn()}, {newbook.get_title()} by {newbook.get_publisher()} has been added to the DB :)")


def custRegister(cust_dict):
    try:
        cID = input("Enter Customer ID: ").title()

        while cID.isalnum() or ((len(cID) == 1) is True) is not True:
            if cID.isalnum() and ((len(cID) > 1) is True):
                break
            else:
                print("ID starts with letter then number(s) ")
                cID = input("Enter Customer ID: ").title()

        cname = input("Enter Customer Name: ").title()
        while cname.isalpha() is not True:
            print("Only letters allowed")
            cname = input("Enter Customer Name: ").title()
            if cname.isalpha() is True:
                break

        email = input("Enter Customer Email: ")
        while (email.__contains__('@') or email.endswith('.com')) is False:
            print("Invalid email format")
            email = input("Enter Customer Email: ")
            if (email.__contains__('@') and email.endswith('.com')) is True:
                break

        tier = input("Enter Tier(A/B/C/D): ").upper()
        tierlist= ['A', 'B', 'C', 'D']
        tCheck = None
        if tier in tierlist:
            tCheck = True
        else:
            tCheck = False

        while tCheck is not True:
            if tier in tierlist is True:
                break
            else:
                print("Tier entered not found")
                tier = input("Enter Tier(A/B/C/D): ").upper()

        pts = input("Enter Points: ")
        while pts.isdigit() != True:
            if pts.isdigit() == True:
                pts = int(pts)
                break
            else:
                print("Enter digits only")
                pts = input("Enter points")
    except Exception as e:
        print(f"Error found: {e}")

    newCust = Customer(cID, cname, email, tier, pts)
    cust_dict[newCust.get_cID()] = newCust
    print(f"Customer of ID {newCust.get_cID()}, Name: {cname} has been made\n")


def custRequest(cQueue, cust_dict):
    cID = input("Enter Customer ID: ").title()

    clist = []
    for key in cust_dict:
        clist.append(key)

    checker = None
    i = None
    if cID in clist:
        checker = True
    else:
        checker = False

    while checker is False:
        print("Customer ID does not exist, try again")
        cID = input("Enter Customer ID: ").title()
        if cID in clist:
            break

    cReq = input("Enter Customer's Request: ")
    cust_dict[cID].set_request(cReq)
    print("Customer's request added successfully\n")

    # cQueue.enqueue(cust_dict[cID])
    nlist = [cust_dict[cID].get_cID(), cust_dict[cID].get_name(), cust_dict[cID].get_email(), cust_dict[cID].get_tier(),
             cust_dict[cID].get_points(), cust_dict[cID].get_request()]

    cQueue.enqueue(nlist)

    return cust_dict, cQueue


# view requests and dequeue
def viewRequest(cust_dict, cQueue):
    peekReq = cQueue.peek()
    jlist = []
    jlist.append(peekReq)
    table = tabulate(jlist, headers=['ID', 'Name', 'Email', "Tier", 'Points', 'Request'], tablefmt='grid')
    print(table)

    cQueue.dequeue()

    print(f'\nRemaining request(s): {cQueue.__len__()}\n')


def updateRequest(cust_dict, cQueue):
    cID = input("Enter Customer ID: ").title()
    while cID.isalnum() is False or cQueue.seqValid(cID) is False:
        if cID.isalnum() is False:
            cID = input("Customer ID starts with letter then number: ").title()
        elif cQueue.seqValid(cID) is False:
            cID = input("Customer ID doesn't exist, try again: ").title()
        elif cID.isalnum() is True and cQueue.seqValid(cID) is True:
            break

    cReq = input("Enter Customer's Updated Request: ")
    cust_dict[cID].set_request(cReq)
    print("Customer's request updated successfully\n")

    cQueue[cID].set_request()
    return cust_dict, cQueue
