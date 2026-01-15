The objective of the task is to fetch the student information data from api then calculate the avg score and then creating bar charts to visualize ,I will use here publicly available Mocki data.The pipeline will for the program is data api fetching,data validation,average calculation then visualization.I will break the problem in multiple modules for readability 

Api_client.py :- fetching and normalising datas
processor.py:- computational of average
visualizer.py:- to do the visualization in bar and plots
main.py:-main module controlling the flow

We are using the api available 
https://dummyjson.com/products

We treat rating as a “test score”
We treat title as a “student identifier”

As it is a products rating the students name might appear as product one as we are using it as the names
