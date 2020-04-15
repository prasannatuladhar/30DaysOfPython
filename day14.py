"""
CSV file in iris.csv

sepal_length,sepal_width,petal_length,petal_width,species
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
4.6,3.1,1.5,0.2,Iris-setosa
5,3.6,1.4,0.2,Iris-setosa
7,3.2,4.7,1.4,Iris-versicolor
6.4,3.2,4.5,1.5,Iris-versicolor
6.9,3.1,4.9,1.5,Iris-versicolor
5.5,2.3,4,1.3,Iris-versicolor
6.5,2.8,4.6,1.5,Iris-versicolor
6.3,3.3,6,2.5,Iris-virginica
5.8,2.7,5.1,1.9,Iris-virginica
7.1,3,5.9,2.1,Iris-virginica
6.3,2.9,5.6,1.8,Iris-virginica
6.5,3,5.8,2.2,Iris-virginica

"""


with open("iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()   #converting csv into list


headers = iris_data[0].strip().split(',') #getting heading of CSV

irises = []   #list where we want to store final result in dic [{}]

for row in iris_data[1:]:
	iris = row.strip().split(",") #geting first data after header 
	iris_dict = dict(zip(headers, iris)) #combing header and firt data into dictionary
	irises.append(iris_dict)  #completing loop for other data remaining

print(irises)

#Excercise
# https://blog.tecladocode.com/python-30-day-14-files/
#  f = open("hello_world.txt", "w")
#  f.write("Hello, World!")
#  f.close()

with open("./hello_world.txt",'w') as file_me:
    file_me.write("Hello,World!")

with open("./hello_world.txt",'a') as file_me:
    file_me.write("\nHow are You?")    

with open("./store.csv",'w') as store:
    store.write(str(irises))    