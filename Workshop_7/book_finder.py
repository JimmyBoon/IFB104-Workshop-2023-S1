#---------------------------------------------------------------------
#
# Book Finder
#
# This exercise gives you practice at extracting elements from web
# documents and using them to create your own HTML file.
#
# Here we will extract some simple elements from the Project Gutenberg
# web site.  Project Gutenberg is an online library of books which
# are in the public domain and hence are free to download.  Its
# home page displays several of the latest books added to the library.
# Our goal is to extract the titles and authors of the latest
# three books and write them to a new web document.
#
# By examining the HTML source code of the Project Gutenberg home page
# (https://www.gutenberg.org/), we can discover that the latest
# book titles and authors appear in the following mark-up:
#
#   <h5>TITLE by AUTHORS</h5>
#
# These fifth level headings are easy to find because there
# are no other mark-ups of this form in the page.
# 
# Your task is to extract details of the three latest books
# marked-up in this way and use them to generate a new web
# document that lists them.  The generated document must contain
# all the standard sections used in HTML documents.
#
# Complete the code below by replacing the "pass" statements.
#

# Import the necessary URL function
from urllib.request import urlopen

# ----------
# Step 1: Get the source HTML document

# Open and download the source document from Project Gutenberg
def get_source_code(website_path):
  gutenberg_file = urlopen(website_path)
  gutenberg_raw_bytes = gutenberg_file.read()
  gutenberg_source_code = gutenberg_raw_bytes.decode("UTF-8")
  gutenberg_file.close()
  return gutenberg_source_code


# ----------
# Step 2: Extract the first three book's titles & authors
gutenberg_source_code = get_source_code('https://www.gutenberg.org/')

# Define the HTML tags we want to find in the source document
def create_book_list():
  open_tag = "<h5>"
  close_tag = "</h5>"

  prev_book_end = 0
  book_list = []


  for i in range(0,3):
    book_start = gutenberg_source_code.find(open_tag, prev_book_end) + 4
    book_end = gutenberg_source_code.find(close_tag, book_start)
    book_list.append(gutenberg_source_code[book_start : book_end])
    prev_book_end = book_end
  
  return book_list

my_book_list = create_book_list()

books_html = f'''<!DOCTYPE html>

<!-- This is an automatically generated HTML document -->

<html>

  <head>
      <title>New Books from Project Gutenberg</title>
  </head>
  
  <body>
  
      <h1>New Books available from
      <a href="https://www.gutenberg.org/">Project Gutenberg</a></h1>

      <!-- The following list was extracted automatically from
           https://www.gutenberg.org/ -->

      <ol>
        <li>{my_book_list[0]}</li>
        <li>{my_book_list[1]}</li>
        <li>{my_book_list[2]}</li>
      </ol>

  </body>
</html>'''


# Replace the three placeholders with the actual book details



# ----------
# Step 4: Write the target HTML document

# Open the target HTML file for writing as Unicode
target_file = 'new_books.html'
books_file = open(target_file, 'w', encoding = 'UTF-8')

# Write the document's contents to the file and tell the
# user
books_file.write(books_html)
print('\nDone!\n\nYou can view the output in file', target_file, '\n')

# Close the target HTML file (which you can now view in
# your favourite web browser)
books_file.close()