
import datetime

corprationName = "East Repair Inc."
corprationAddress = "1912 Harvest Lane New York, NY 12210"
now = datetime.datetime.now()


class invoiceApp:
    serial= "A"
    counter = int("0123456789")
    def __init__(self):
        self.billTo = ""
        self.shipTo = ""
        self.taxNo = ""
        self.items = []
        self.taxRate = 0.0625
        self.generator = ""
    
    def generate_serial(self):
        num = 123456789
        while True:
            yield "A" + str(num).zfill(9)
            num += 1
    def get_next_serial(self):
        return next(self.generator)


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
        print("Invoice Date: ", now)
        print("Invoice #: ", get_next_serial())
        print("===================\n")

        print("Qty\tDescription\tUnit Price\Amount")
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
