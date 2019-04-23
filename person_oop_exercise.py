class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 

        # Add a friends instance variable (attribute) to the Person class. You will initialize it to an empty list within the constructor __init__
        self.friends = []

        # We want to count the number of times a person has greeted someone. To do this, we'll add another attribute, call it say greeting_count, and initialize it to 0. Then each time the greet method is called, we'll increment greeting_count by 1.
        self.greeting_count = 0
        self.greeted_people = []

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

        if other_person.name not in self.greeted_people:
            self.greeted_people.append(other_person.name)

        self.greeting_count += 1
    
    # Add a print_contact_info method to the Person class that will print out the contact info for a object instance of Person
    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}' .format(self.name, self.email, self.name, self.phone))

    # Implement an add_friend method to Person, so that in order to add a friend
    def add_friend(self,friend):
        self.friends.append(friend)
    
    # Implement a num_friends method which returns the number of friends the person currently has
    def num_friends(self):
        print(len(self.friends))
    
    # Keep track of the number of unique people a person has greeted, and be able to report that number via the num_unique_people_greeted method
    def num_unique_people_greeted(self):
        print(len(self.greeted_people))

# 1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
sonny = Person('Sonny','sonny@hotmail.com.com','483-485-4948')

# 2. Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jordan','jordan@aol.com','495-586-3456')

dee_ann = Person('Dee Ann','da@aol.com','495-586-1234')

# 3. Have sonny greet jordan using the greet method.
sonny.greet(jordan)

# 4. Have jordan greet sonny using the greet method.
jordan.greet(sonny)

# 5. Write a print statement to print the contact info (email and phone) of Sonny.
print('Email: {} Phone: {}'.format(sonny.email,sonny.phone))

# 6. Write another print statement to print the contact info of Jordan.
print('Email: {} Phone: {}'.format(jordan.email,jordan.phone))

sonny.print_contact_info()

jordan.friends.append(sonny)
sonny.friends.append(jordan)

print(len(jordan.friends))
print(len(sonny.friends))

jordan.add_friend('rj')

jordan.num_friends()

sonny.greet(jordan)
print(sonny.greeting_count)

print(jordan)
print(str(jordan))

sonny.num_unique_people_greeted()

sonny.greet(dee_ann)

sonny.num_unique_people_greeted()