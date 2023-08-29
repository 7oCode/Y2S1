from Book_Functions import *
from Book_Functions import *
from Customer import *


def BookStore():

    book_dict = {}
    cust_queue = Queue()
    cust_dict = {}
    stop = True
    while stop:
        try:
            print("Welcome to book store:\n"
                  "1: Add Book Manually\n"
                  "2: Sort books by Category in ascending order using Bubble sort\n"
                  "3: Sort books by Publisher in descending order using Selection sort\n"
                  "4: Sort books by Title in ascending order using Insertion sort\n"
                  "5: Sort books by Year Published and ISBN in ascending order using Merge sort\n"
                  "6: Manage Customer request \n"
                  "7: Show all books\n"
                  "8: Export to excel sheet\n"
                  "9: Populate Books with data\n"
                  "0: Exit\n")
            choice = int(input("\nSelect a number: "))
        except ValueError:
            print("Only Numbers\n")
        else:
            if choice == 1:
                createBook(book_dict)

            elif choice == 2: # Bubble Sort, Category   D O N E
                blist = []
                if len(book_dict) == 0:
                    print("No books made yet, press 1\n")

                bubblesort(blist, book_dict)

            elif choice == 3: # Selection Sort, Publisher D O N E
                blist = []
                if len(book_dict) == 0:
                    print("No books made yet, press 1\n")

                selection_sort(blist, book_dict)

            elif choice == 4:
                # Title, ascending, insertion sort D O N E
                blist = []
                insertion_slot(blist, book_dict)

            elif choice == 5:
                # Year Published then ISBN, ascending, merge sort D O N E
                if len(book_dict) == 0:
                    print("No books made yet, press 1\n")

                blist = []
                for key in book_dict:
                    blist.append(book_dict.get(key))

                show_merge_sort(blist)

            elif choice == 6:
                # manage request, queue system
                cust_dict, cust_queue = Manage_Requests(cust_dict, cust_queue)

            elif choice == 7: # Display all books D O N E
                blist = []
                if len(book_dict) == 0:
                    print("No books made yet, press 1\n")

                display_books(blist, book_dict)

            elif choice == 8:
                exportExcel(cust_dict,book_dict,cust_queue)

            elif choice == 9:
                new1 = Books("98134", "Backrooms", "Horror", "Kane", "2020")
                new2 = Books("983", "Three Little Pigs", "Kids", "Joseph", "1920")
                new3 = Books("18132", "Alice in Wonderland", "Adventure", "Guy", "2013")
                new4 = Books('71139', "Networking for Dummies", "Education", "Doug Lowe", '2021')
                new5 = Books('91323', "Computer Architecture: A Quantitative Approach", "Education", "John L", '2013')
                # use .title()

                book_dict[new1.get_isbn()] = new1
                book_dict[new2.get_isbn()] = new2
                book_dict[new3.get_isbn()] = new3
                book_dict[new4.get_isbn()] = new4
                book_dict[new5.get_isbn()] = new5
                # createBook(book_dict)
                print(f"{len(cust_dict)} book(s) have been added")

            elif choice == 0: # B Y E
                print("\nSee you next time~")

                break


def Manage_Requests(cust_dict, cust_queue):

    stop = True
    while stop:
        try:
            print("1: Register Customer \n"
              "2: Input customer request \n"
              "3: View number of request(s) \n"
              "4: Service next request in Queue \n"
                "5: Populate Customer Data\n"
              "0: Return to Main Menu\n")

            choice = int(input("Select a number: "))

        except ValueError:
            print("Only Numbers")
        else:
            if choice == 1:
                custRegister(cust_dict)
                print(len(cust_dict))
                print(cust_dict)

            elif choice == 2:
                if len(cust_dict) == 0:
                    print("No customers found, press 1 to register\n")
                else:
                    cust_dict, cust_queue = custRequest(cust_queue, cust_dict)

            elif choice == 3:
                print(f"Number of requests: {cust_queue.__len__()}\n")

            elif choice == 4:
                if cust_queue.__len__() == 0:
                    print("Error, make new requests\n")
                else:
                    viewRequest(cust_dict,cust_queue)

            # elif choice == 5:
            #     updateRequest(cust_dict, cust_queue)

            elif choice == 5:
                c1 = Customer('S11', "Jeff", "Jeff@gmail.com", "A", "1000")
                c2 = Customer("S22", "Guy", "Guy@gmail.com", "B", "750")
                c3 = Customer("S33", "Olfsen", "Olfsen@gmail.com", "C", "500")
                c4 = Customer("S44", "Joe", "Joe@gmail.com", "D", "350")

                cust_dict[c1.get_cID()] = c1
                cust_dict[c2.get_cID()] = c2
                cust_dict[c3.get_cID()] = c3
                cust_dict[c4.get_cID()] = c4
                print(f"{len(cust_dict)} customer(s) have been added")

            elif choice == 0:
                return cust_dict, cust_queue


def exportExcel(cust_dict, book_dict, cust_queue):

    while True:
        try:
            print("1: Export Customer Data \n"
                  "2: Export Books Data \n"
                  "3: Export Queue Data\n"
                  "0: Exit \n")

            choice = int(input("Select a number: "))
        except ValueError:
            print("Only numbers allowed")
        else:
            if choice == 1:
                cdict = {}
                if len(cust_dict) == 0:
                    print("Customer Data is currently empty, make a new customer first")
                else:
                    df = pd.DataFrame()
                    for key in cust_dict:
                        cdict = cust_dict.get(key)
                        df = df._append({"Customer ID": cdict.get_cID(),
                                        "Customer Name": cdict.get_name(),
                                        "Customer Email" :cdict.get_email(),
                                        "Customer Tier": cdict.get_tier(),
                                        "Customer Points": cdict.get_points()},
                                       ignore_index=True)
                    df.to_excel("Customers.xlsx", index=False)
                    print("Export of Customers data into Customers.xlsx is successful!\n")


            elif choice == 2:
                bdict = {}
                if len(book_dict) == 0:
                    print("Book Data is currently empty, add some books first")

                else:
                    df = pd.DataFrame()
                    for key in book_dict:
                        bdict = book_dict.get(key)
                        df = df._append({"ISBN": bdict.get_isbn(),
                                        "Publisher": bdict.get_publisher(),
                                        "Year Published": bdict.get_year_published(),
                                        "Title": bdict.get_title(),
                                        "Category": bdict.get_category()},
                                       ignore_index=True)
                    df.to_excel("Books.xlsx", index=False)
                    print("Export of Books data into Books.xlsx is successful!\n")

            elif choice == 3:
                qdict = {}
                if cust_queue.__len__() == 0:
                    print("Customer Queue is currently empty, add some requests first")
                else:
                    show = cust_queue.show_all()
                    df = pd.DataFrame()
                    for each in range(len(show)):
                        df = df._append({"Customer ID": show[each][0],
                                         "Customer Name": show[each][1],
                                         "Customer Email": show[each][2],
                                         "Customer Request": show[each][-1]},
                                        ignore_index=True)
                    df.to_excel("Queue.xlsx", index=False)
                    print("Export of Queue data into Queue.xlsx is successful!\n")

            elif choice == 0:
                break


BookStore()
