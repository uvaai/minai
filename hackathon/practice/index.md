### Grade Calculator

Write a function `calculate_grade()` that takes one argument: `score`. The function should calculate and return the corresponding letter grade based on the following grading scale:

    Scores from 90 to 100 receive an "A"
    Scores from 80 to 89 receive a "B"
    Scores from 70 to 79 receive a "C"
    Scores from 60 to 69 receive a "D"
    Scores below 60 receive an "F"

For example:

    print(calculate_grade(75))
    print(calculate_grade(39))
    print(calculate_grade(92))

Output:

    C
    F
    A

### Palindrome Checker

Write a Python function `is_palindrome(word)` that takes a string word as input and returns `True` if the word is a palindrome (reads the same forwards and backwards), and `False` otherwise. The input may contain both uppercase and lowercase letters. Your function should ignore capitalization when checking whether the word is a palindrome.

For example, if you call the function like this:

    result1 = is_palindrome("racecar")
    result2 = is_palindrome("hello")
    result3 = is_palindrome("LEVEL")
    result4 = is_palindrome("Otto")

    print(result1)  # Should print True
    print(result2)  # Should print False
    print(result3)  # Should print True
    print(result4)  # Should print True

Which should print:

    True
    False
    True
    True

### Secret message

Write a function `find_secret_message(text)` that accepts a `text`, and finds all characters that directly follow the letter `'p'`. The function should return a list containing these characters. As with the last exercise, the text may contain both uppercase and lowercase letters. Both 'p' and 'P' should be treated as the letter 'p'.

    text = 'Apophenia is not paranoia, it requires sharpness of mind and patience.'
    family = find_secret_message(text)

    print(f"The secret message is: {family}")

Should print:

    The secret message is: ['o', 'h', 'a', 'n', 'a']

### Longest sequence

Write a function called `longest_sequence(lst)` that takes a list (`lst`) as input and returns the *length* of the longest consecutive sequence of the same element. If the list is empty, the function should return 0.

Have a look at this example:

    longest1 = longest_sequence(['a', 'b', 'b', 0])
    longest2 = longest_sequence(['a', 'b', 'b', 0, 0, 0])
    longest3 = longest_sequence([1, 1, 1, 1, 2, 3])

    print(longest1)
    print(longest2)
    print(longest3)

Expected output:

    2
    3
    4

### Repetition

The text `"a aa aa b"` has one sequence that is repeated in direct succession: `"aa"`. For this exercise, a sequence is a group of characters separated by spaces. A repetition occurs when a sequence is directly followed by the same sequence. Each repeated occurrence counts separately, so `"aa aa aa"` contains two repetitions.  
The text `"aa bb aa y"` has no repetitions, because the two occurrences of `"aa"` are not directly next to each other. The text `"x aa aa aa y bb bb"` has three repetitions: `"aa"` is repeated twice, and `"bb"` is repeated once.

Write a function repetition_count(text) that expects a text as input and returns the number of repetitions in direct succession.

    example_text = "x aa aa aa y bb bb"

    print(repetition_count(example_text))

Expected output:

    3

And:

    example_text = "x aa l aa aa y bb bb"

    print(repetition_count(example_text))

Should output:

    2

### Speech synthesis

A number can be divided into digits. For example, the number 423 consists of the digits 4, 2 and 3. We want to use a speech synthesizer to pronounce numbers, digit by digit. So the number 423 should be pronounced as "four", "two", "three". Write a function `number_speech(number)` that accepts a number as an argument, and splits the number into separate digits. The function should return the separate digits as a list, and the result can then be printed as follows:

    number_list = number_speech(1984)

    for number in number_list:
        print(number)

Which should print the following:

    one
    nine
    eight
    four

**Hint:** remember that you can access the individual characters in a _string_ in the same way you can get the individual elements from a list.

### Grade calculator v2

The keys in the dictionary are tuples containing the lowest and highest score for a grade, and the values are the corresponding letter grades.

Write a function `calculate_grade(grade_dict, score)` that accepts a grade dictionary and a score as input. The function should find the range that contains the score and return the corresponding grade. Both the lowest and highest score in a range should be included.

If the score does not fall within any of the ranges, the function should return `"No matching grade"`.

Have a look at this example:

    grade_dict = {
        (0, 59): "F",
        (60, 69): "D",
        (70, 79): "C",
        (80, 89): "B",
        (90, 100): "A"
    }

    print(calculate_grade(grade_dict, 78))
    print(calculate_grade({(89, 90): "Test"}, 89))
    print(calculate_grade({(89, 90): "Test"}, 90))
    print(calculate_grade({(89, 90): "Test"}, 91))

This should produce the output:

    C
    Test
    Test
    No matching grade


### Booklist

For school, you are required to read books from a prescribed booklist. Instead of asking you to read at least 5 books from that list, the teacher asks you to read at least 1000 pages. Of course, even though you are an eager student, you don't want to read way too much. Write a function `count_pages(books_page_count, read_books)` that, given a dictionary of books (with the title of the book as a key, and the number of pages in that book as value) and a list of titles you have read, can calculate the total number of pages in the books that you have read. You may assume that all titles in `read_books` occur in `books_page_count`.

    books_page_count = {'Nineteen Eighty-Four': 328, 'The Very Hungry Caterpillar': 22, 'Gulliver\'s Travels': 352, 'Frankenstein': 280, 'David Copperfield': 624, 'Moby-Dick': 736, 'Ulysses': 730, 'Lord of the Flies': 224, 'To Kill a Mockingbird': 281, 'The Picture of Dorian Gray': 272,'The Hobbit': 310}

    read_books = ['The Very Hungry Caterpillar', 'The Hobbit', 'Frankenstein', 'Lord of the Flies']

    page_total = count_pages(books_page_count, read_books)
    print(f'The books {read_books} have {page_total} pages in total.')


Should print:

    The books ['The Very Hungry Caterpillar', 'The Hobbit', 'Frankenstein', 'Lord of the Flies'] have 836 pages in total.

### Expense

You're writing a program that keeps track of your expenses. You're using a dictionary that keeps track of the monthly expenses in euros per category (_food_, _rent_, _internet_, _utilities_, _social activities_, etc.). Now you would like to know what percentages of your monthly expenses these categories represent.

Write a function  `euros_to_percentage(expenses)` that accepts a dictionary containing the expenses in euros. It should create a new dictionary containing the expenses in percentages.

Have a look a this example:

    expenses_january_in_euros = {'rent': 735, 'utilities': 221,
                                 'food': 167, 'social activities': 185,
                                 'internet + netflix + spotify': 58, 'phone': 25}
    expenses_january_in_percentages = euros_to_percentage(expenses_january_in_euros)
    print(expenses_january_in_percentages)

This should produce the output:


    {'rent': 52.83968368080517, 'utilities': 15.88785046728972, 'food': 12.005751258087706, 'social activities': 13.299784327821712, 'internet + netflix + spotify': 4.169662113587347, 'phone': 1.7972681524083394}


**Note:** the order in which this result is printed does not need to be the same as the example above. Check whether each category has the right value. If this is the case, your code probably works!

### Movie Ratings

You are given a list of movie ratings, and you want to calculate statistics based on these ratings. Write a function called `calculate_movie_stats(ratings)` that takes a dictionary `ratings` as input, where the keys are movie names, and the values are lists of ratings for each movie.

The function should calculate the following statistics for each movie:

    The average rating
    The highest rating
    The lowest rating

The function should return a new dictionary where the keys are the movie names and the values are dictionaries containing the calculated statistics.

For example, if you call the function like this:

    ratings = {
        'Movie1': [4.5, 3.2, 4.0, 3.8, 4.7],
        'Movie2': [3.0, 3.5, 2.8, 3.2, 2.5],
        'Movie3': [4.8, 4.5, 4.9, 4.7, 4.6]
    }

    movie_stats = calculate_movie_stats(ratings)
    print(movie_stats)

It should output:

    {
        'Movie1': {'average_rating': 4.04, 'highest_rating': 4.7, 'lowest_rating': 3.2},
        'Movie2': {'average_rating': 3.0, 'highest_rating': 3.5, 'lowest_rating': 2.5},
        'Movie3': {'average_rating': 4.7, 'highest_rating': 4.9, 'lowest_rating': 4.5}
    }


### Finish the booklist

Write a new function named `done_reading(books_page_count, read_books)`. Using the `count_pages` function from before, check if the total number of pages in the books you have read is at least 1000. If this is the case, the function should print `"Total pages is {total}. All done"`. If not, find the shortest book that you have not yet read that would bring the total to at least 1000 pages, and recommend that book to the user.

    done_reading(books_page_count, ['The Picture of Dorian Gray'])
    done_reading(books_page_count, ['Nineteen Eighty-Four', 'Gulliver\'s Travels', 'The Hobbit'])

Should output:

    Your current total is 272. Read Ulysses of 730 pages to complete your list.
    Your current total is 990. Read The Very Hungry Caterpillar of 22 pages to complete your list.
