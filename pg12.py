#Write a program that checks if two lists have at least one element in common using sets. 
thislist1 = ["red","orange","blue","green"]
thislist2 = ["yellow","black","green","rose"]


set1 = set(thislist1)
set2 = set(thislist2)

if set1.intersection(set2):
    print("The lists have at least one element in common.")
else:
    print("The lists have no elements in common.")
