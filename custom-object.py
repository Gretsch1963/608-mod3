#JohnHickman#
# Python Custom Object representing a purchase for a specific amount
class Purchase(object):
    def __init__(self,amount):
        self.amount = amount

    def calculateTax(self, taxPercent):
        return self.amount * taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount * tipPercent/100.0

    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount * (1 + taxPercent/100.0 + tipPercent/100.0)

# Create the purchase object for a given amount
purchase = Purchase(100.0)

# Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Use the purchase object to calculate tax and tip
tax = purchase.calculateTax(taxPercent)
tip = purchase.calculateTip(tipPercent)

#Display outputs
print ('Tax Amount: ', tax)
print ('Tip Amount: ', tip)
print ('Total Amount: ', purchase.calculateTotal(taxPercent, tipPercent))

#John Hickman#
