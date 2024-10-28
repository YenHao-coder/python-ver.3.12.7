def greet():
    print(f'Hello, what is your name? ')
    print('Where are you from? ')
    print('What is your habbit? ')
greet()

 #多個參數以上的函式
def greet_with(name, location):
    print(f"Hello {name}. ")
    print(f"What is it like in {location}? ")
greet_with("Bob", "Nowhere")
greet_with("Nowhere", "Bob")
greet_with(location = "Nowhere", name ="Bob")
