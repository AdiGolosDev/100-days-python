states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

#index error /// list has items from index 0 -- 49 \ nothing at index 50
# print(states_of_america[50])

fruits = ["cherry", "apple", "pear"]
vegetables = ["cucumber", "kale", "spinnach"]
fruits_and_vegetables = [fruits, vegetables]

for item in fruits_and_vegetables:
     for i in item:
        print(i)

for item in fruits_and_vegetables:
    print(item)

print(fruits_and_vegetables[1][2])