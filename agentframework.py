import random 

class Agent():            #create a new class 
    def __init__ (self, environment, agents):   #self represents the object 
        self.environment = environment 
        self.store = 0 #give the sheep empty stomachs 
        self._x = random.randint(0,300)  #create self._x and assign a value - 
        #use underscore to protect both self.x and self.y from being changed 
        self._y = random.randint(0,300) #create self._y and assign a value
        self.agents = agents #list of agents into each agent 
  
    
    def move (self): #create a move function 
        if random.random() < 0.5:
            self._x = (self._x + 3) % 299 #using a torus boundary of 299 means 
        else:                           #the agents never leave the animation 
            self._x = (self._x - 3) % 299   #because if they go beyond the left 
        if random.random() < 0.5:           #hand side they will re-enter on 
            self._y = (self._y + 3) % 299   #the right hand side for example 
        else:
            self._y = (self._y - 3) % 299 
  
      
    def eat(self):
        if self.environment[self._y][self._x] > 10: #if the environment of the
                                            #agent is equal to more than 10:
           self.environment[self._y][self._x] -= 10  #minus 10 from the 
                                                       #environment 
           self.store += 10 #add 10 to the sheeps store
           
        if 0 < self.environment[self._y][self._x] < 10: #if the environment has
                                                        #less than 10 units:
           self.store += self.environment[self._y][self._x] #add the entire 
           #environment to the sheeps store
           self.environment[self._y][self._x] -= self.environment[self._y][self._x]
           #empty the environment so it is equal to 0
        
        
    def sick(self):
        if self.store > 500: #if sheep has stored more than 500 it will sick 
                            #it back up
           self.environment[self._y][self._x] = self.environment[self._y][self._x] + self.store     
           #add the self store back into the environment
           self.store = 0 #empty the self store 
           
    def run (self):     
        if self.store > 250: #if the sheep has a store exceeding 250:
            self._x = (self._x + 20) % 299 #make the sheep move further along 
                                            #the x axis
        if self.store > 250: #if the sheep has a store of more than 250:  
            self._y = (self._y + 20) % 299 #make the sheep move further along 
                                            #the y axis
          
    def share_with_neighbours (self, neighbourhood): 
        for agent in self.agents: #for all agents
            dist = self.distance_between(agent) #dist = the distance between 
                                                #agents
        if dist <= neighbourhood:   #if the distance between the agents is less
        #than or equal to the neighbourhood (specified on Model script):
            sum = self.store + agent.store #add the self store and the 
                                            #neighbouring agents store
            average = sum / 2 #calculate the average of the stores 
            self.store = average #set the self store to the average 
            agent.store = average #set the neighbouring agents store to the 
                                    #average also 

    #make a function declaration to calculate the distance between the agents 
    #called during the share_with_neighbours above

    def distance_between(self, agent):
        return (((self._x - agent._x)**2) + ((self._y - agent._y)**2))**0.5
        
        
            
  
        
        
        
#
#as each agent changes the environment (because the environment is a mutable 
#object - a list) and the variable is therefore a link to the object passed in, 
#all the agents link to the same environment object. As the agents change the 
#environment data, it changes for all the agents. If environment object was an
#immutable object, this wouldnt be the case as changing it would result in a 
#new copy being created
#
