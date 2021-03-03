"""
This keyword argument unpacking syntax can be used even if the function takes other parameters. However,
the parameters must be listed in this order:

    All named positional parameters
    An unpacked positional parameter (*args)
    All named keyword parameters
    An unpacked keyword parameter (**kwargs)

Here’s a function with all possible types of parameter:

def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []

  if '-a' in args:
    user_list = all_users()

  if kwargs.get('active'):
    user_list = [user for user_list if user.active]

  with open(filename) as user_file:
    user_file.write(user_list)

Looking at the signature of main() we define four different kinds of parameters. The first, filename is a normal
required positional parameter. The second, *args, is all positional arguments given to a function after that
organized as a tuple in the parameter args. The third, user_list, is a keyword parameter with a default value.
Lastly, **kwargs is all other keyword arguments assembled as a dictionary in the parameter kwargs.

A possible call to the function could look like this:

main("files/users/userslist.txt",
     "-d",
     "-a",
     save_all_records=True,
     user_list=current_users)

In the body of main() these arguments would look like this:

    filename == "files/users/userslist.txt"
    args == ('-d', '-a)
    user_list == current_users
    kwargs == {'save_all_records': True}

We can use all four of these kinds of parameters to create functions that handle a lot of possible arguments being
passed to them.
"""


def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()
        for arg in args:
            text = text.replace(arg, '')
        for kwarg, replacement in kwargs.items():
            text = text.replace(kwarg, replacement)
    return text


print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))
