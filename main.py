from random import randint


def distribute_books(book):
    # Initialize the Total Pages with 0
    total_pages = sum(book)

    # Get the average number of pages per employee
    avg_pages = total_pages // 3

    # Each employee will represent a section and we initialize them
    section_pages = 0
    section_count = 0
    desired_value = -1

    # Go through every book in the list
    for i in range(len(book)):
        # For every book, we add its pages to the section total page sum
        section_pages += book[i]

        # Find the point where adding another book exceeds the average pages count
        if i + 1 < len(book) and section_pages + book[i + 1] > avg_pages:
            # Find the number of pages before adding another book
            before_avg = section_pages

            # Find the number of pages after adding another book
            after_avg = section_pages + book[i + 1]

            # Find whether it's worth adding another book to the section or not
            if abs(avg_pages - before_avg) > abs(avg_pages - after_avg):
                # If the after_avg page count is closer to avg_pages
                desired_value = after_avg
            else:
                # If the before_avg page count is closer to avg_pages
                desired_value = before_avg

        # Print each book's page count
        print(book[i], end=' ')

        # If the page count in the current section reaches the desired value, and we have less than 3 sections
        if section_pages == desired_value and section_count < 2:
            # Separate sections with a "-"
            print("- ", end='')

            # Reset pages and desired value
            section_pages = 0
            desired_value = -1

            # Move onto the next section
            section_count += 1


# Initialize a "book" array which contains the page count of every book
#book = [100, 200, 300, 400, 500, 600, 700, 800, 900]

# Initialize a "book" array with random amount of books.
# Comment the next 4 lines and uncomment the one above for preset number of books
book = []
no_books = randint(5, 25)
for i in range(0, no_books):
    book += [randint(1, 10000)]

# Call the function that solves the problem
distribute_books(book)
