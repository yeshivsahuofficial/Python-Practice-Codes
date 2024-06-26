course={
    'Python': {'Fee':9000,'Duration':'2 Months'},
    'C': {'Fee': 8000, 'Duration': '2 Months'},
    'Java': {'Fee': 10000, 'Duration': '2 Months'}
}
print(course)

#Python course
print(course['Python'])
#C course
print(course['C'])
#Java course
print(course['Java'])
#Iteration
for k,v in course.items():
    print(k,v['Duration'],v['Fee'])

# course={
#     'Python': {'Fee':9000,'Duration':'2 Months'},
#     'C': {'Fee': 8000, 'Duration': '2 Months'},
#     'Java': {'Fee': 10000, 'Duration': '2 Months'}
# }

print(f"Java fee price is:{course['Java']['Fee']}")    #Java Fee amount
#Changing value of Java Fee to 9500
course['Java']['Fee']=9500
print(f"After changing Fee amount the price is:{course['Java']['Fee']}")
