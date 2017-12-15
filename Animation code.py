
import random #so we can randomise values 
import operator #to enable us to use item getter 

import matplotlib.pyplot #allows to make graphs 
import matplotlib.animation
import agentframework
import csv

'''
import matplotlib
matplotlib.use('macosx') 
If using a Mac you can use the above two lines of code to get the animation 
to run outside of the console
'''
num_of_agents = 10 #add a variable that will control the number of agents 
                    #that are created
num_of_iterations = 100 #set the number of movements to 100
neighbourhood = 20 #add a new variable 'neighbourhood' 
                    #and assign it a value of 20 
environment = [] #create empty environment list which the downloaded 
                #environment file 'in.txt' can be added to
agents = [] #Create an empty 'agent' list
distance_list = [] #create an empty 'distance' list that the distances between 
                    #agents will later be added into
store = 0   #add a variable 'store' and assign it a value of 0


#Code below sets up the graph for the animation which is produced later 
fig = matplotlib.pyplot.figure(figsize=(7, 7)) 
ax = fig.add_axes([0, 0, 1, 1]) 

#Creating the environment:
f = open('in.txt', newline='') #open in.txt - the csv that provides the 
                                #environment
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC) #read in the file and 
                                                    #convert the numbers into 
                                                    #floats 
for row in reader: #python intrinsically knows what a row is, so it picks out 
                    #each row in the reader file 
    rowlist = [] #create an empty list called rowlist 
    for item in row: #python also knows what an item is, this code sets it up 
                    #to identify each item in the row 
        rowlist.append(item) #each item is not assigned to a row, and then 
                            #assigned to the rowlist
    environment.append(rowlist)#assign the rowlist to the environment
f.close() #close the 'in.txt' as now have a completed environment


'''
when appending items to the rowlist:
so theres loads of rows in the original file (in.txt) which within the 
environment are put into [] when you print it. when you print the rowlist at 
the end of this you will only see one row in [] because it creates a new one 
everytime in the loop so it will be the last row created in the loop
'''


#Making the agents:
for i in range(num_of_agents): #create a for-loop to create as many agents as 
                                #we like - specified by num_of_agents
    agents.append(agentframework.Agent(environment, agents)) #we have created 
    #the Agent class in the agent framework so call on it here


#Animation
def update(frame_number):
    
    fig.clear() #clear the figure created above so its empty
    random.shuffle(agents) #randomly shuffle the agents so they move, eat etc.
                            #in a random order
                            
    for i in range(num_of_agents): #call the functions from the agent framework 
        agents[i].move()            #to give the agents behaviours and make
        agents[i].eat()             #them interact with eachother 
        agents[i].sick() 
        agents[i].share_with_neighbours(neighbourhood)
       
        matplotlib.pyplot.xlim(0, len(environment)) #set the x axis  
        matplotlib.pyplot.ylim(0, len(environment)) #set the y axis 
        matplotlib.pyplot.imshow(environment) #plot the environment
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x, agents[i]._y, color='white') 
        #for the number of agents (10) plot their x - 'agent[i]._x' - and 
        #y - 'agent[i]._y' - coordinates making them white dots 

animation = matplotlib.animation.FuncAnimation(fig, update, 
                                               interval=1, 
                                               repeat=False, 
                                               frames=num_of_iterations)

#create the animation, using the number of iterations as the number of 
#frames (the animation will stop when the sheep have moved 100 times); the 
#'update' calls the contents of the animation (because have been defined in
#"def update(frame_number):" above)

fig.show() #show the animation



#Write out the final environment - this will be different from the 'in.txt' 
#as the sheep have eaten away at the environment
f2 = open('environmentout.csv', 'w', newline='')#open a csv for the environment
writer = csv.writer(f2, delimiter=' ')#right the csv using comma seperated
for row in environment: 
    writer.writerow(row) #assign each row in the environment to the csv
f2.close()#close the csv
