    # {"title": "Book Name1", "author": "author1", "release_year": 2008},
reading_list = []

def add_book():
    title=input("Enter a title of book : ")
    author=input("Enter a Author of book : ")
    release_year=input("Enter a Release year of book : ")

    reading_list.append(
        {
        "title":title,
        "author":author,
        "release_year":release_year
        }
    )



def display_book():
    for v in reading_list:
        print(f"{v['title']} ({v['release_year']}) - {v['author']}")




user_choice= input("Make a choice. A for Add to list , D for display result and Q for quit : ")
while user_choice != 'q' or user_choice !='Q':
    if user_choice == "a" or  user_choice == "A":
        add_book()
    elif user_choice == 'D' or user_choice == 'd':
        display_book()
    else:
        print("Invalid Choice")  
    user_choice= input("Make a choice. A for Add to list , D for display result and Q for quit : ")


    