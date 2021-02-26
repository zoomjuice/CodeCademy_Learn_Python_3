"""
You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list
 object. Each element of the dict_list returned by .items() is a tuple consisting of:

(key, value)

so to iterate through, you can use this syntax:

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
"""

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37,
                           "Aerospace Engineer": 9}

for occ, pct in pct_women_in_occupation.items():
    print('Women make up {percent} percent of {occupation}s.'.format(percent=pct, occupation=occ))
