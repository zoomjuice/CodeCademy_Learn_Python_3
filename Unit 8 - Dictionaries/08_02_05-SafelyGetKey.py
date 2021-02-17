"""
Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the
 key you are trying to .get() does not exist, it will return None by default.

You can also specify a value to return if the key doesn't exist. For example, we might want to return a building height
 of 0 if our desired building is not in the dictionary.
"""

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931,
            "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder', 100_000)
print(tc_id)

stack_id = user_ids.get('superStackSmash', 100_000)
print(stack_id)
