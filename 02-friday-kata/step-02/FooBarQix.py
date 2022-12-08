class FooBarQix:
    
    def say_hello( time_of_day):
        if(time_of_day == "morning"):
            return "Good Morning"
        
        elif(time_of_day == "night"):
            return "Good Night"
        else:
            raise Exception("unexpected keyword")

