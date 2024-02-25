my_dict = {
    "bakery": ["bread", "rolls", "donut"],
    "grocery store": ["carrots", "celery", "arugula"]
}
for product in my_dict:
    print(f'I am going to the {product} where I will buy {my_dict[product]}')
x = 0
for word in my_dict.values():
    x = x + len(word)
print(f'I am buying {x} items')
print("I am making a change to this file")
numbers = []
for i in range(0,30):
    if i %2 == 0:
        numbers.append[i]
        
