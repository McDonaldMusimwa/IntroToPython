class IntroClass:

    def __init__(self,name) -> None:
        self.name = name

    def introduceUser(self):
        namelength = len(self.name)
        print ("**"+(namelength * '*')+ "**")
        print   (f"* {self.name} *")  
        print ("**"+(namelength * '*')+ "**")