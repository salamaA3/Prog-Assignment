class Customer:
    def __init__(self, customer_id, name, contact, address):
        self.customer_id = customer_id
        self.name = name
        self.contact = contact
        self.address = address

    def get_details(self):
        return f"Customer: {self.name}, Contact: {self.contact}, Address: {self.address}"

    def update_address(self, new_address):
        self.address = new_address


class Item:
    def __init__(self, item_code, description, quantity, unit_price):
        self.item_code = item_code
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = self.calculate_total()

    def calculate_total(self):
        return self.quantity * self.unit_price


class DeliveryOrder:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []
        self.total_price = 0
        self.delivery_status = "Pending"

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.total_price

    def update_status(self, status):
        self.delivery_status = status

    def generate_delivery_note(self):
        return DeliveryNote(self)


class DeliveryNote:
    def __init__(self, order):
        self.note_id = f"DN-{order.order_id}"
        self.order = order
        self.date = "January 25, 2025"
        self.recipient_details = order.customer.get_details()

    def generate_note(self):
        print(f"Delivery Note: {self.note_id}\nDate: {self.date}\nRecipient: {self.recipient_details}")
        print("Items:")
        for item in self.order.items:
            print(f"{item.item_code} - {item.description}: {item.quantity} x {item.unit_price} = {item.total_price}")
        print(f"Total Price: AED {self.order.total_price}")


# Example Usage
customer = Customer("C001", "Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")
order = DeliveryOrder("DEL123456789", customer)
order.add_item(Item("ITM001", "Wireless Keyboard", 1, 100))
order.add_item(Item("ITM002", "Wireless Mouse & Pad Set", 1, 75))
order.add_item(Item("ITM003", "Laptop Cooling Pad", 1, 120))
order.add_item(Item("ITM004", "Camera Lock", 3, 15))
note = order.generate_delivery_note()
note.generate_note()