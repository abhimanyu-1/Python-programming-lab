class  Time():

    def __init__(self, hours, minutes,sec):
        self.hours = hours
        self.minutes = minutes
        self.sec=sec

    def addTime(t1, t2):
        
        t3 = Time(0, 0,0) # creating new object
        t3.hours = t1.hours + t2.hours # sum of hours
        t3.minutes = t1.minutes + t2.minutes # sum of minutes
        t3.sec=t1.sec+t2.sec
        
        while t3.sec>=60:
            t3.minutes += 1
            t3.sec -= 60
        return t3
    
        while t3.minutes >= 60:
            t3.hours += 1
            t3.minutes -= 60
        return t3
    
     

    def displayTime(self):
        print("Time is %d hours and %d minutes %d second" %(self.hours, self.minutes,self.sec))

a = Time(2,40,30)
b = Time(1, 10,40)
c = Time.addTime(a,b)

c.displayTime()
