#views.py 
from django.shortcuts import render 
def fruits_and_students(request): 
print(request.build_absolute_uri()) 
fruits = ['Apple', 'Banana', 'Orange', 'Grapes'] 
students = ['Alice', 'Bob', 'Charlie', 'David'] 
return render(request, 'fruits_and_students/fruits_and_students.html', {'fruits': fruits, 
'students': students})
