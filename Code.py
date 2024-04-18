#CODE IS AS ::
class Package:
     packageval=0
     def __init__(self,packageNo):
         self.packageval=packageNo
         if(packageNo<=6):
             print("There are",packageNo,"items are in the package has been shipped out")
         elif(packageNo>6):
            print("The maximum items limit has been exceeded,",packageNo-6,"items must be removed from the package")
               
#MAIN FUNCTION IS MADE AND SOLVED        
if __name__=="__main__":
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn=input("Ship more packages?Y/N ")
        morepackages=yn=='y' or yn=='Y'
 