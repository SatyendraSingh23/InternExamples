class Node : 
	def __init__(self,data) :
		self.data=data
		self.next=None

class LinkedList :
	def __init__(self) :
		self.head=None
	def add(self,data) :
		node=Node(data)
		if self.head==None : 
			self.head=node
			return
		temp=self.head
		while temp.next!=None :
				temp=temp.next #temp = 1004
		temp.next=node
	def printAll(self) :
		if self.head==None :
			print("Empty LinkedList , Please get Lost ! ")
			return
		temp=self.head
		while temp!=None :
			print(temp.data)
			temp=temp.next

lst=LinkedList()
lst.add(10)
lst.add(20)
lst.add(30)
lst.add(40)
lst.add(50)
lst.printAll()