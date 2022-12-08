class Greeter:
    
    def say_hello(moment):
        if(moment=="morning"):
            return "Good Morning"
        elif(moment=="night"):
            return "Good Night"
        else:
            raise Exception("unexpected moment")

