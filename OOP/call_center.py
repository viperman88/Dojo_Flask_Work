from datetime import datetime

class Call(object):
    uniqueID = 0

    def __init__(self,name,phone_num,reason):
        self.name = name
        self.phone_num = phone_num
        self.time = datetime.now()
        self.reason = reason
        Call.uniqueID += 1

    def display(self):
        print "ID: " + str(self.uniqueID)
        print "Name: " + self.name
        print "Number: " + str(self.phone_num)
        print "Time: " + self.time.strftime("%I:%M:%S")
        print "Reason: " + self.reason
        print ""
        return self

call1 = Call("Robert Amato","512-678-8790","Customer service")
call1.display()

call2 = Call("Maggie Amato","210-345-1234","Stock info")
call2.display()

call3 = Call("Franklin Amato","210-345-1234","Stock info")
call3.display()

call4 = Call("Mama Amato","654-876-1234","Career info")
call4.display()

call5 = Call("Ashley Amato","453-183-7465","Stock info")
call5.display()

class CallCenter(object):

    def __init__(self):
        self.calls = []
        #self.queue = self.queue_size()

    def queue_size(self):
        return len(self.calls)

    def add(self,new_call):
        self.calls.append(new_call)
        return self

    def remove(self,old_call):
        self.calls.remove(old_call)
        return self

    def info(self):
        for call in self.calls:
            call.display()

center = CallCenter()
center.add(call1).add(call2)
center.add(call3).add(call4).add(call5)
center.remove(call1)
print "Queue size: " + str(center.queue_size())
