
from abc import ABC, abstractmethod

class CustomerManagement:
    def __init__(self, name, customer_id, email):
        self.name = name
        self.id = customer_id
        self.email = email
        self.bookings = []

    def book_ticket(self, booking):
        self.bookings.append(booking)

    def view_bookings(self):
        return self.bookings

class TicketManagement(ABC):
    def __init__(self, unique_id, price):
        self.unique_id = unique_id

        if price <= 0:
            print("Price must be greater than zero")
            self.price = 0
        else:
            self.price = price

        self.is_booked = False

    @abstractmethod
    def calculate_price(self):
        pass

    def __str__(self):
        return (
            f"Ticket ID: {self.unique_id}, "
            f"Price: ₹{self.calculate_price()}"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(id={self.unique_id}, price={self.price})"
        )

    def __eq__(self, other):
        if not isinstance(other, TicketManagement):
            return NotImplemented

        return self.unique_id == other.unique_id

class RegularTicket(TicketManagement):
    def __init__(self, unique_id, price, waiting_time, seat_facility):
        super().__init__(unique_id, price)
        self.waiting_time = waiting_time
        self.seat_facility = seat_facility

    def calculate_price(self):
        return self.price

class VIPTicket(TicketManagement):
    def __init__(self, unique_id, price, waiting_time,
                 seat_facility, discount):
        super().__init__(unique_id, price)

        self.waiting_time = waiting_time
        self.seat_facility = seat_facility

        if discount < 0 or discount > self.price:
            print("Invalid discount")
            self.discount = 0
        else:
            self.discount = discount

    def calculate_price(self):
        return self.price - self.discount
class EventManagement:
    def __init__(self, name, event_id, venue):
        self.name = name
        self.event_id = event_id
        self.venue = venue
        self.available_tickets = []

    def add_ticket(self, ticket):
        if not ticket.is_booked and ticket not in self.available_tickets:
            self.available_tickets.append(ticket)

    def get_remaining_tickets_count(self):
        return len(self.available_tickets)

    def __len__(self):
        return len(self.available_tickets)
class BookingManagement:
    def __init__(self, booking_id, customer, ticket, event):
        self.booking_id = booking_id
        self.customer = customer
        self.ticket = ticket
        self.event = event
        self.is_active = False

    def confirm_booking(self):

        if self.ticket.is_booked:
            print("Ticket already booked")
            return False

        if self.ticket not in self.event.available_tickets:
            print("Ticket unavailable for this event")
            return False

        if self.ticket.price <= 0:
            print("Invalid ticket price")
            return False

        self.ticket.is_booked = True
        self.event.available_tickets.remove(self.ticket)

        self.customer.book_ticket(self)
        self.is_active = True

        print("Booking successful")
        return True

    def cancel_booking(self):

        if not self.is_active:
            print("Invalid cancellation")
            return False

        self.ticket.is_booked = False
        self.event.add_ticket(self.ticket)

        if self in self.customer.bookings:
            self.customer.bookings.remove(self)

        self.is_active = False

        print("Booking cancelled")
        return True


customer1 = CustomerManagement(
    "Monster", 101, "monster@gmail.com"
)

event1 = EventManagement(
    "Gaming Fest", 501, "Hyderabad"
)

ticket1 = RegularTicket(1, 500, 10, "Normal Seat")
ticket2 = VIPTicket(2, 1000, 5, "Premium Seat", 200)

event1.add_ticket(ticket1)
event1.add_ticket(ticket2)

booking1 = BookingManagement(
    1001, customer1, ticket1, event1
)

booking1.confirm_booking()

print("Remaining tickets:", len(event1))
print("Customer bookings:", customer1.view_bookings())

booking1.cancel_booking()

print("Remaining tickets:", len(event1))

print("\n--- DUNDER METHOD TESTING ---")

print(ticket1)

print(repr(ticket2))

print(len(event1))

ticket3 = RegularTicket(1, 700, 5, "Normal Seat")
print(ticket1 == ticket3)  
print(ticket1 == ticket2)  
