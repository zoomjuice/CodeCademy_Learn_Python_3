"""
Python also provides a handy string method for including variables in strings. This method is .format().
 .format() takes variables as an argument and includes them in the string that it is run on. You include {} marks as
 placeholders for where those variables will be imported.

 def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

 print(favorite_song_statement("Smooth", "Santana"))
 # => "My favorite song is Smooth by Santana"

.format() can be made more legible by including keywords. Previously, you had to make sure that your variables appeared
 as arguments in the same order that you wanted them to appear in the string.

By including keywords in the string and in the arguments, you can remove that ambiguity. Let’s look at an example.

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)

Now it is clear to anyone reading the string what it supposed to return, they don’t even need to look at the arguments
 of .format() in order to get a clear understanding of what is supposed to happen. You can even reverse the order of
 artist and song in the code above and it will work the same way. This makes writing AND reading the code much easier.
"""


# 6.2.11


def poem_title_card(title, poet):
    return 'The poem "{}" is written by {}.'.format(title, poet)


print(poem_title_card("I Hear America Singing", "Walt Whitman"))


# 6.2.12


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}."\
        .format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc


my_beard_description = poem_description('1974', 'Shel Silverstein', 'My Beard', 'Where the Sidewalk Ends')
print(my_beard_description)
