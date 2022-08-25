class Faculty: 
  #a=["java","c++","webdev","python"]
  b={"java":"divi","c++":"shlok","webdev":" ","python":"ram"}

  def __init__(self,subjects,teachers):

   self.subjects=subjects
   self.teachers=teachers

  def Display(self):
    print(self.b.keys())

  def Apply(self):
    for key,value in self.b.items():
        if value==" ":
            print(key)
            
  def Ad(self):
    x=input("Enter the subject name:")
    for key in self.b.keys():
        if key==x:
            print("Subject is already present.")
            
    
        else:
            self.b[x]=" "
            
  def Resign(self):
      y=input("Enter the name of the teacher.")
      for a in self.b.values():
          if a==y:
              print("The teacher has been removed")
         
          
       

f=Faculty("c","d") 

n=0

while n==0:
  print("(1)Display subjects")
  print("(2)Apply")
  print("(3)Add subjects")
  print("(4)Resign")
  print("(5)Exit")
  a=int(input("Enter your choice:-"))

  if a==1:
    f.Display()

  elif a==2:
    f.Apply()

  elif a==3:
    f.Ad()

  elif a==4:
    f.Resign()
             

  else:
    n=1





  






