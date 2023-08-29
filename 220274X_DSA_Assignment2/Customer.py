class Queue():
    def __init__(self):
        self.__queue = []

    def isEmpty(self):
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def __len__(self):
        return len(self.__queue)

    def enqueue(self, item):
        return self.__queue.append(item)

    def peek(self):
        return self.__queue[0]

    def show_all(self):
        return self.__queue

    def dequeue(self):
        assert not self.isEmpty(), \
        "Cannot dequeue from an empty queue"

        self.__queue.pop(0)
        return self.__queue

    def seqValid(self, nCheck):
        stop = False

        for a in range(len(self.__queue)):
            if nCheck == self.__queue[a].get_cID():
                stop = True
                break

        if stop == True:
            print(F"Invalid, {nCheck} already exists")
            return True
        else:
            return False

    def __str__(self):
        return self.__queue

    def point(self,index):
        return self.__queue[index]


class Customer():
    count = 0
    def __init__(self, cID,name, email, tier, points):
        self.__cID = cID
        self.__name = name
        self.__email = email
        self.__tier = tier
        self.__points = points
        self.__request = None

    def set_request(self,req):
        self.__request = req

    def get_request(self):
        return self.__request

    def get_cID(self):
        return self.__cID

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_tier(self):
        return self.__tier

    def get_points(self):
        return self.__points
