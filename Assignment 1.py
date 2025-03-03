class Customer:
    """Represents a customer with personal details."""
    def __init__(self, customer_id, name, contact, address):
        # Initialize customer attributes
        self.customer_id = customer_id  # Unique ID for the customer
        self.name = name  # Customer's name
        self.contact = contact  # Customer's contact information (email/phone)
        self.address = address  # Customer's address

    def get_details(self):
        # Returns formatted string containing customer details
        return f"Customer: {self.name}, Contact: {self.contact}, Address: {self.address}"

    def update_address(self, new_address):
        # Updates the customer's address
        self.address = new_address


class Item:
    """Represents an item in a delivery order."""
    def __init__(self, item_code, description, quantity, unit_price):
        # Initialize item attributes
        self.item_code = item_code  # Unique code identifying the item
        self.description = description  # Short description of the item
        self.quantity = quantity  # Number of items being ordered
        self.unit_price = unit_price  # Price per single unit
        self.total_price = self.calculate_total()  # Calculate total price for the item

    def calculate_total(self):
        # Computes total price of the item based on quantity and unit price
        return self.quantity * self.unit_price


class DeliveryOrder:
    """Handles the details of a delivery order."""
    def __init__(self, order_id, customer):
        # Initialize delivery order attributes
        self.order_id = order_id  # Unique order identifier
        self.customer = customer  # Customer associated with the order
        self.items = []  # List to store items in the order
        self.total_price = 0  # Initialize total price of the order
        self.delivery_status = "Pending"  # Default delivery status

    def add_item(self, item):
        # Adds an item to the order and updates the total price
        self.items.append(item)
        self.total_price += item.total_price

    def update_status(self, status):
        # Updates the delivery status of the order
        self.delivery_status = status

    def generate_delivery_note(self):
        # Creates a DeliveryNote object for the order
        return DeliveryNote(self)


class DeliveryNote:
    """Generates a delivery note for an order."""
    def __init__(self, order):
        # Initialize delivery note attributes
        self.note_id = f"DN-{order.order_id}"  # Delivery note ID, prefixed with "DN-"
        self.order = order  # The associated delivery order
        self.date = "January 25, 2025"  # Fixed date for the note (can be dynamic)
        self.recipient_details = order.customer.get_details()  # Fetch customer details

    def generate_note(self):
        # Prints the formatted delivery note details
        print(f"Delivery Note: {self.note_id}\nDate: {self.date}\nRecipient: {self.recipient_details}")
        print("Items:")
        for item in self.order.items:
            # Prints each item's details
            print(f"{item.item_code} - {item.description}: {item.quantity} x {item.unit_price} = {item.total_price}")
        print(f"Total Price: AED {self.order.total_price}")


# Example Usage
# Create a customer object
customer = Customer("C001", "Sarah Johnson", "sarah.johnson@example.com", "45 Knowledge Avenue, Dubai, UAE")

# Create a delivery order for the customer
order = DeliveryOrder("DEL123456789", customer)

# Add items to the order
order.add_item(Item("ITM001", "Wireless Keyboard", 1, 100))
order.add_item(Item("ITM002", "Wireless Mouse & Pad Set", 1, 75))
order.add_item(Item("ITM003", "Laptop Cooling Pad", 1, 120))
order.add_item(Item("ITM004", "Camera Lock", 3, 15))

# Generate and display the delivery note
note = order.generate_delivery_note()
note.generate_note()
