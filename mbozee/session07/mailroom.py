#!/usr/bin/env python3


class Donor:
    '''Donor has a name.'''
    def __init__(self):
        self.name = ''

    def say_hello(self):
        return "My name is " + self.name + "."


def menu():
    """Print out list of options."""
    print("menu>>   <name>:add donor and donation   l:list donors   r:print report   t:thank you   h:help   q:quit")

donors = {
    'Donovan Leitch': [100, 20, 1000],
    'Stevie Nicks': [200, 500],
    'Ian Anderson': [190],
    'Mavis Staples': [170, 40, 130],
    'Suzanne Vega': [160, 300]
}


def thank_you(name, value):
    """Compose and print thank you letter."""
    letter = '''
    Dear {},

    Thank you for your generous donation of ${}.
    Your gift makes a major impact on aspiring musicians in the Seattle area.

    Sincerely,
    Seattle Music Fund
    '''.format(name, value)
    print(letter)


def create_report():
    """Generate a report of donors and donation amounts."""
    donors_sorted = sorted(donors.items(),
                           key=lambda t: sum(t[1]), reverse=True)

    print("Donor Name                | Total Given | Num Gifts | Avg Gift")

    for donor in donors_sorted:
        print("{} | {} | {} | {}".format(
            donor[0].ljust(25),
            str(sum(donor[1])).rjust(11),
            str(len(donor[1])).rjust(9),
            str(round(sum(donor[1])/len(donor[1]))).rjust(8)
        ))

    print('\n', end='')
    menu()


def list():
    """Print a list of donor names."""
    for donor in donors:
        print(donor)


def help():
    """Print basic instructions."""
    print("""Mailroom is a program for managing donation records and sending thank you letters to donors.
          Use the menu to start a process.""")


def add_donation(new_donor, new_amount):
    """Add donation entry into donors dictionary."""
    donors[new_donor] = [new_amount]

    while True:
        new_amount = int(input("mailroom >>   How much is {} donating? ".format(new_donor)))

        if new_amount >= 0:
            break
        else:
            print("Amount must not be negative!")
            continue

if __name__ == '__main__':
    menu()

    while True:
        user_input = input('mailroom>>   ')

        if user_input == 'q' or user_input == 'quit':
            break

        if user_input == 'l' or user_input == 'list donors':
            list()
            continue

        if user_input == 'r' or user_input == 'create report':
            create_report()
            continue

        if user_input == 't' or user_input == 'thank donors':
            entry = [thank_you(name, sum(value)) for name, value in donors.items()]
            continue

        if user_input == 'h' or user_input == 'help':
            help()
            continue

        new_donor = user_input

        while True: # This prompts user for input twice... but validates against non-positive donations.
            new_amount = int(input("mailroom >>   How much is {} donating? ".format(new_donor)))
            if new_amount > 0:
                break

        add_donation(new_donor, new_amount)