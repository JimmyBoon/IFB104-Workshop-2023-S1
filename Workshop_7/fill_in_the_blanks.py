#---------------------------------------------------------------------
#
# Fill-in-the-Blanks Story
#
# As a simple example of generating an HTML document using Python,
# here you will create a children's story using words supplied by
# the user to fill in the blanks.
#
# The story in this case is "The Witch Next Door" from the "Activity
# Village" web site (https://www.activityvillage.co.uk/).
#
# Your task is to develop a program which prompts the user for six
# words and uses these words to fill in the blanks in the story
# below.  You must then create an HTML file containing the completed
# story.  To ensure that the story is formatted nicely, you will need
# to add some HTML tags into the text provided below.
#

# This is the text of the story with the blanks marked WORD1 to
# WORD6.  You can add HTML tags into the text as necessary to
# make it display nicely in a web browser.
the_story = '''
The Witch Next Door

Sam and Amy lived next door to a very strange old woman. She always wore
a black crooked hat, she kept a black cat, and she'd give a cackling laugh
whenever she spoke. On Halloween, they decided to knock on her door to see
if she would give them any lollies. But when she opened the door she said,
"Like lollies, do you? Well, I'd better give you some then."

There was a puff of smoke and Sam realised that his WORD1 had
turned into a WORD2! There was another puff of smoke and Amy
had a huge WORD3 where her WORD4 had been!

Just as there was another puff, the black cat jumped up into the smoke. When
it fell down to the ground it had turned into a very large, cross-looking
WORD5. The WORD5 chased the old woman back into her house,
clawing at her WORD6.

Sam and Amy's bodies went back to normal after a while, but they didn't eat a
WORD2 or WORD3 for a long time afterwards!
'''

# Get the six words from the user, which will be used in place of the
# blanks in the story.  The words needed to complete the story are:
#
# 1. A part of the body
# 2. A lolly (sweet)
# 3. A chocolate bar
# 4. Another body part
# 5. An animal you'd find in a pet shop other than a cat
# 6. An item of female clothing
#
word1 = "Arm"
word2 = "Gummy Bear"
word3 = "Chocolate"
word4 = "Leg"
word5 = "Dog"
word6 = "Dress"

word_list = ["Arm","Gummy Bear","Chocolate","Leg","Dog","Dress"]
replace_list = ["WORD1", "WORD2", "WORD3", "WORD4", "WORD5", "WORD6"]


for i in range(0, len(word_list)):
    the_story = the_story.replace(replace_list[i], word_list[i])


# Replace the "blank" placeholders in the story
story_html = f'''<!DOCTYPE html>

<!-- This is an automatically generated HTML document -->

<html>

  <head>
      <title>The Story</title>
  </head>
  
  <body>
    <p>{the_story}</p>
  </body>
</html>'''



target_file = 'story.html'
story_file = open(target_file, 'w', encoding = 'UTF-8')

# Write the document's contents to the file and tell the
# user
story_file.write(story_html)
print('\nDone!\n\nYou can view the output in file', target_file, '\n')

# Close the target HTML file (which you can now view in
# your favourite web browser)
story_file.close()

