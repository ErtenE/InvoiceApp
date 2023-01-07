
import datetime
import pymongo
import psycopg2


corprationName = "East Repair Inc."
corprationAddress = "1912 Harvest Lane New York, NY 12210"
now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%d %H:%M:%S')
num = 1234567890
counter = 0

class invoiceApp:
   
    def __init__(self):
        self.billTo = ""
        self.shipTo = ""
        self.taxNo = ""
        self.items = []
        self.taxRate = 0.0625
        self.counter = 0
        self.num= 1234567890
        self.generator = self.generate_serial()
    


    def generate_serial(self):
    # Increment the counter
        self.counter += 1
        # Concatenate the counter with the base number to create the serial number
        serial = f"{self.num}{self.counter:05d}"
        return serial

    
    def CustomerInformation(self):
        self.billTo = input("Enter Billing Name: ")
        self.shipTo = input("Enter Addresss: ")
        self.taxNo = input("Enter Tax Number: ")
    
    

    def salesItem(self):
        try:
            qty = int(input("Qty: "))
            description:str = (input("Enter Description: "))
            unitPrice = float(input("Enter Unit Price: "))
            self.items.append((qty, description, unitPrice))
        except ValueError:
            print("Invalid input. Please enter a valid quantity and unit price.")

        
    print("INVOICE APPLICATION")
    print("===================================")

    def generateInvoice(self):
        total = 0
        print(f"Bill To: {self.billTo}")
        print(f"Ship To: {self.shipTo}")
        print(f"Tax Number: {self.taxNo}")

        print("===================")
        print("\nSales Invoice\n")
        print("===================\n")
        print(corprationName)
        print(corprationAddress+"\n")
        print("Invoice Date: ", date_time)
        print("Invoice #:", self.generator)
        print("===================\n")

        print("Qty\tDescription\tUnit Price\tAmount")
        for item in self.items:
            qty, description, unitPrice = item
            total += qty * unitPrice
            print(f"{qty}\t{description}\t\t{unitPrice:.2f}\t\t{qty * unitPrice:.2f}")
        tax = total * self.taxRate
        print(f"\nTax: {tax:.2f}")
        print(f"\nTotal: {total + tax:.2f}")
app = invoiceApp()
app.CustomerInformation()

while True:
    app.salesItem()
    response = input("Add another item? (y/n)")
    if response.lower() == "n":
        break



app.generateInvoice()


