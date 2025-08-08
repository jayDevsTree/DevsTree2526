import random # for generate fare Price
class Train:
    isBooked = False# this not acceseble direct in class method we need className_AttributeName = Train.isBooked = True
                    # purpose this attribute is acceble all objects of class (class attributes)
    def __init__ (self):
        self.trainNo = int(input("Enter Train Number:"))
        self.isTicketBooked = False# this can acceseble in all methods in class
                                   # purpose to access instance attributes 
                                        
        
    def bookTicket (self):
        self.fromm = input("Enter From:")
        self.to = input("Enter To:")
        self.seatCategory = input("Enter Coach:")
        print("Ticket Booked!")
        self.isTicketBooked = True
        # Train.isBooked = True
        # print(f'Ticket Booked! --> TrainNo = {self.trainNo}')
        
    def ticketStatus(self):
        if self.isTicketBooked == True:
            print(f'Status --> From: {self.fromm}, To: {self.to}, Coach: {self.seatCategory}, TrainNo = {self.trainNo}')
            print('Booked!')
        
        # if Train.isBooked == True:
        #     print('Status --> Booked!')
        #     print(f'From:{self.fromm} , To:{self.to} , Coach:{self.seatCategory} , TrainNo = {self.trainNo}')
        
        # if self.bookTicket() == True:
        #     print('Status --> Booked!')
        #     print(f'From:{self.fromm} , To:{self.to} , Coach:{self.seatCategory} , TrainNo = {self.trainNo}')
        else:
            print("Status --> Ticket Not Booked")
            
    def ticketFair(self):
        self.fair = random.randint(150,6500)
        print(f"Fair -->{self.fromm} to {self.to} in {self.seatCategory} coatch fair = {self.fair}")
        
t1 = Train()
t1.bookTicket()
t1.ticketFair()
t1.ticketStatus()