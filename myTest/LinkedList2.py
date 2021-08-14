class Node : 
	def __init__(self,data) :
		self.data=data
		self.next=None
class LinkedList :
	def __init__(self) :
		self.start=None
	def add(self,data) :
		node = Node(data)
		if self.start==None :
			self.start=node
		else :
			tmp=self.start
			while tmp.next!=None :
				tmp=tmp.next
			tmp.next=node
	def insert_at(self,pos,data) :
		node=Node(data)
		if self.start==None :
			self.start=node
			return
		tt=None
		tmp=self.start
		p=1
		if pos<=0 or pos==1 :
			node.next=self.start
			self.start=node
			return	
		while p!=pos-1 and tmp.next!=None :
			 tmp=tmp.next
			 p=p+1
		tt=tmp.next
		tmp.next=node
		node.next=tt

	def printAll(self) :
		if self.start==None : 
			print("Empty List, Please get Lost.")
			return
		tmp=self.start
		while tmp!=None :
			print(tmp.data)
			tmp=tmp.next
"""           1     2     3      4    5        
 	start ->1000-> 10 -> 20 -> 30 -> 40 -> 50 ->None 
 	store value of next section of node which is at position 2, Lets store in variable name tt
 	p=2
 	tmp=20
"""

lst=LinkedList()
req=int(input("Enter the requiremnet."))
if req<=0 :
	print("Invalid requirement.")
else :	
	i=0;
	while i!=req :
		data=int(input("Please Enter a number."))
		lst.add(data)
		i=i+1;       
	
	lst.printAll() 

print("------------------Linked List successfully Created -----------")
p=int(input("Enter the position."))
data=int(input("Please Enter a number."))
lst.insert_at(p,data)
lst.printAll()





"""
 1) If linked List is null and user is inserting element at a certain position
	 For Ex:- lst.insert(3,100)
    Solution : insert element on first position
 2) If User is giving position exceeding the length of linked list 
	 For Ex:-List.length is 2, lst.insert(10,100)
    Solution : insert element on last position
 3) If User is giving negative position  
	 For Ex:- lst.insert(-1010,100)
    Solution : insert element on first position
"""