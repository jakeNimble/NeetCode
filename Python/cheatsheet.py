#CheatSheet

#Dictionary (also know as a hashmap):
  #Creation: 
    CharMaps = {}
    #Can use 
      charMaps = defaultdict(list) 
      #to make it so the dictionary automatically creates a key value pair with an empty list (or w/e I choose)
  #Appending:
    CharMaps["thing"] = "this"
  #Checking Existence:
    if "thing" in CharMaps:
  #Update
    my_dict.update({"b": 2})  # Adds "b" to the dictionary
    #Can be used to create or to update a dictionary


#List:
  #Creation
    #list can be created with just [0,1]
    myList = []
  #append
  myList.append(k)
  #Enumerate:
    #Use this when you want to iterate over a list and reference the indices
    for j, num in enumerate(nums):
  
  



#Useful Python Functions:
  #Sorted: takes any iterable (e.g., a string, list, tuple, etc.) and returns a new sorted list of its elements.
    result = sorted("hello")
    print(result)  # Output: ['e', 'h', 'l', 'l', 'o']
  #join: 
    #method takes a list (or any iterable) of strings and combines them into a single string. 
    "".join(['a', 'e', 't'])  # Output: "aet"


  
