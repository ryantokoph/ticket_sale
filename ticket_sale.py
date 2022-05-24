
TICKET_PRICE = 10

SERVICE_CHARGE = 2

tickets_remaining = 100

def calculate_price(num):
    return (num * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets left".format(tickets_remaining))
    name = input("What is your name? ")
    num_tickets = input("Hi {}, how many tickets do you want? ".format(name))
    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There aren't that many tickets available")
    except ValueError as err:
        print("Oh no! We ran into an issue. {} Please try again.".format(err))
    else:
        ticket_cost = calculate_price(num_tickets)
        print("{} tickets will cost ${}.".format(num_tickets, ticket_cost))
        proceed = input("Would you like to proceed? Enter Y/N: ")
        if proceed.upper() == "Y":
            print("Sold!")
            tickets_remaining -= num_tickets
        else:
            print("Thanks {}, come again!".format(name))
print("Tickets are sold out!")
    