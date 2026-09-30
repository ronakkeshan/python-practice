class Invoice:
    def __init__(self,Date,Invoice_id,Customer_name,Base_amount,Gst_tax_rate):
        self.date=Date
        self.invoice_id=Invoice_id
        self.customer_name=Customer_name
        self.base_amount = Base_amount
        self.gst_tax_rate=Gst_tax_rate

    def get_total(self):
       total=self.base_amount+(self.base_amount*self.gst_tax_rate)
       return total   

    def get_gst_amount(self):
        return self.base_amount * self.gst_tax_rate     

    def __str__(self):
      return f'{self.customer_name} — Invoice {self.invoice_id}, dated {self.date}, with a base amount of ₹{self.base_amount} and a GST rate of {int(self.gst_tax_rate*100)}%.'

class DiscountedInvoice(Invoice):
    def __init__(self, Date, Invoice_id, Customer_name, Base_amount, Gst_tax_rate,Discount_rate):
        super().__init__(Date, Invoice_id, Customer_name, Base_amount, Gst_tax_rate)
        self.discount_rate=Discount_rate

    def get_total(self):
       discount=self.base_amount-(self.base_amount*self.discount_rate)
       total=discount+(discount*self.gst_tax_rate)
       return total 

    def get_gst_amount(self):
        discounted_base = self.base_amount - (self.base_amount * self.discount_rate)
        return discounted_base * self.gst_tax_rate

    def __str__(self):
        base_str = super().__str__()
        return base_str + f' Discount applied: {int(self.discount_rate*100)}%.'

def calculate_gst(invoices):
    total = 0
    for i in invoices:
        try:
            total += i.get_gst_amount()
        except (TypeError, AttributeError):
            print("data error")
    return total



invoice1 = Invoice("30-09-2026", "INV001", "Ravi", 10000, 0.18)

invoice2 = DiscountedInvoice(
    "30-09-2026",
    "INV002",
    "Amit",
    20000,
    0.18,
    0.10
)

invoices = [invoice1, invoice2]

print(invoice1)
print(invoice2)

print(invoice1.get_total())
print(invoice2.get_total())

print(calculate_gst(invoices))