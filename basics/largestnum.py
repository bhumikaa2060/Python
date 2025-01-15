import utils

numbers = [10, 3, 6, 2]

max = utils.find_max(numbers) #max become integer so we cant call max function here only if we comment this line we can usse max  function
print(max)

#python also has max function built in you can simply use it as:
#print(max(numbers))