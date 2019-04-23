class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0
        self.greeted_people = []

    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

    def greet(self, other_person): 
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

        if other_person.name not in self.greeted_people:
            self.greeted_people.append(other_person.name)

        self.greeting_count += 1

    def print_contact_info(self):
        print('{}\'s email: {}, {}\'s phone number: {}' .format(self.name, self.email, self.name, self.phone))

    def add_friend(self,friend):
        self.friends.append(friend)
    
    def num_friends(self):
        print(len(self.friends))
    
    def num_unique_people_greeted(self):
        print(len(self.greeted_people))

sonny = Person('Sonny','sonny@hotmail.com.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
dee_ann = Person('Dee Ann','da@aol.com','495-586-1234')

sonny.greet(jordan)
jordan.greet(sonny)

print('Email: {} Phone: {}'.format(sonny.email,sonny.phone))
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