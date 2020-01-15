import pandas as pd

names = ["arie", "thomas","Koen"]

names_list =["arie","thomas"]
ages_list =[29, 32]
people_dict = {"name" : names_list, 
               "age": ages_list}

#print("this is the dico \n{} \n".format(people_dict))

personen_df = pd.DataFrame(people_dict)
print(personen_df)
