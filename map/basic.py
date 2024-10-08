'''
    map takes in function and collection 
    and iterates all elements one by one 
    over that function
    - map can also be used to map out 2
    different parameters from 2 different 
    collections over a function
    $ map(function,iterable)
'''
# print('--'*25)
# list_of_numbers = [i for i in range(10)]
# output_of_map = list(map(lambda x: x**2,list_of_numbers))
# # syntax map(function,list/iterable)
# print(output_of_map)

# print('--'*25)
# def add_square(x,y):
#     return(x**2 + y**2)
# list_A = [i for i in range(1,6)]
# list_B = [i for i in range(6,11)]
# print(list_A + list_B)
# output_of_map_2 = list(map(add_square,list_A,list_B))
# print(output_of_map_2)

# '''
#     task1
#     read two list from user
#     if same element of two list is 10 then concatinate them
#     eg: 1+9 = 19
# '''
# def conList (x,y):
#     if x + y == 10:
#         return str(x) + str(y)



# N = int(input('Enter number of element to input: '))
# listA = [ int(input(f'For List 1 element {1+i}: ')) for i in range(N)]
# listB = [ int(input(f'For List 2 element {1+i}: ')) for i in range(N)]

# output_of_map = list(map(conList,listA,listB))
# print(output_of_map)


'''
    Filter:
        filter works very similar to map
        it takes function and iterable as input
        returns output whenever it is true
        $ map(function,iterable)
'''
# print('=='*25)
# numbers = [i for i in range (10)]
# evenMap = list(map(lambda x: x%2==0,numbers))
# evens = list(filter(lambda x: x%2 == 0, numbers))
# print(evenMap)
# print(evens)

# '''
#     given a listA create another list containig elements with 
#     length more than 3
# '''
# listA = ['apple','ball','cat','dog','elephant']
# outputList = list(filter(lambda x: len(x)>3,listA))
# print(outputList)

'''
    Reduce:
        [1,2,3,4]
        multiply(x,y) ->x*y
        it runs the function one by one in cumulative way from left
            to right
        

        $ reduce(function,iterable,iterable_value)
'''
# from functools import reduce

# print('--'*25)
# listA = [i for i in range(1,6)]
# outputList =  reduce(lambda x,y: x*y,listA)
# print(outputList)

# '''
#     task 
#     create list from user 
#     pass it to function square_and_add4(x)
#     using map create transition list passing over the function
#     using filter create another list that accepts divisible by five
# '''
# N = int(input('Enter number of element to input: '))
# userList = [ int(input(f'For List 1 element {1+i}: ')) for i in range(N)]
# outputMap = list(map(lambda x:x**2+4,userList))
# outputFilter = list(filter(lambda x: x%5 == 0,outputMap))
# outputReduce = reduce(lambda x,y:x+y,outputFilter)
# print(userList)
# print(outputMap)
# print(outputFilter)
# print(outputReduce)

'''
    Decorators:
        - Decorators are special functions that takes in other functions as parameter
        - Decorators are initialized with @
'''
print('--'*25)
# def smartConversion( func):
#     def wrapper(x,y):
#         return func(int(x),int(y))
#     return wrapper

# @smartConversion #decorator function
# def division(x,y):
#     return x/y

# @smartConversion
# def addition(x,y):
#     return x+y

# print(division('4','2'))
# print(addition('4','2'))
# print('--'*25)

# import time

# def counter(func):
#     def wrapper(n):
#         start = time.time()
#         func (n)
#         end = time.time()
#         return(end - start)
#     return wrapper

# @counter
# def largeComputation (n):
#     random_computaion = 0
#     for i in range (0,n):
#         for j in range (0,n):
#             random_computaion +=1
#     return random_computaion

# print(largeComputation(100))

'''
    task
        function for add,sub,div,mult
        should only have return statement

        create decorateor named identify_function_and_parameters that should display 
        which function is running and what is parameter
'''

def identify_function_and_parameters(func):
    def wrapper(x,y):
        print(f'function name: {func.__name__}\nparameters: {x}, {y}')
        return func(x,y)
    return wrapper

x = 9
y = 3
@identify_function_and_parameters
def addition(x,y):
    return x+y

@identify_function_and_parameters
def subtraction(x,y):
    return x-y

@identify_function_and_parameters
def multiplication(x,y):
    return x*y

@identify_function_and_parameters
def division(x,y):
    return x/y

print(addition)
print(multiplication)
print(subtraction)
print(division)