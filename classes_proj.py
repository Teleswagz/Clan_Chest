# Jack M. Ormond
# Project 6
# Due: Friday, December 9th, 2016, 11:59pm
#
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#
# References: Zybooks, Professor Mark Snyder's lectures and slides
#
# 

class Book:
	
	def __init__(self, author, title, book_id):
		
		self.author = author
		self.title = title
		self.book_id = book_id
		
	def __str__(self):
	
		return ("Book(\"%s\", \"%s\", %d)" %
		(self.author, self.title, self.book_id))
	
	def __repr__(self):
		
		return str(self)
	
	def __eq__(self, other):
		return (self.author==other.author and self.title==other.title and
		self.book_id==other.book_id)
#create Patron class		
class Patron:
	#Patron constructor 
	def __init__(self, name, patron_id, borroweds = None):
		if borroweds == None:
			borroweds = []
		self.name = name
		self.patron_id = patron_id 
		self.borroweds = borroweds 
	#string representation of variables 
	def __str__(self):
		answer = """Patron("%s", %d, [""" % (self.name, self.patron_id)
		#loops through borrowed list 
		for i in range(len(self.borroweds)):
			if i != len(self.borroweds) - 1:
				answer += (self.borroweds[i].__str__() + ', ')
			else:
				answer += (self.borroweds[i].__str__())
			
		answer += '])'
		return answer
	#computer use representation 
	def __repr__(self):
		return str(self)
	#reshelves book tries to and has exception if doesn't work
	def return_book(self, library, book_id):
		try:
			library.reshelve_book(self.patron_id, book_id)
			return True
		except:
			return False
	#checks book out of library using book's id tries to and has exception
	#if doesn't work
	def check_out_book_by_id(self, library, book_id):
		try:
			library.loan_book(self.patron_id, book_id)
			return True
		except:
			return False
	#same as check book by id but with title 
	def check_out_book_by_title(self, library, title):
		
		book = library.book_by_title(title)
		try:
			library.loan_book(self.patron_id, book.book_id)
			return True
		except:
			raise LookupError('no book found with the title "%s"' % (title))
			return False
#class for handling duplicate id error		
class DuplicateIdError (Exception):
	
	def __init__(self, id, category = "Book"):
		self.id = id
		self.category = category 
		
	def __str__(self):
		if self.category == 'Book':
			return ('duplicate Book ID: #%d' % (self.id)) 
		return ('duplicate Patron ID: #%d' % (self.id))
	
	def __repr__(self):
		return str(self)
#class for handling missing id error
class MissingIdError (LookupError):
	
	def __init__(self, id, category = "Book"):
		self.id = id
		self.category = category 
		
	def __str__(self):
		if self.category == 'Book':
			return ('Book #%d not found' % (self.id))
		return ('Patron #%d not found' % (self.id))
		
	def __repr__(self):
		return str(self)
#creates class for library 
class Library:
	#constructor for library class 
	def __init__(self, books = None, patrons = None):
		self.books = books 
		self.patrons = patrons 
		if self.books == None:
			self.books = [] 
		if self.patrons == None:
			self.patrons = []
	#string representation for class' variables 
	def __str__(self) : 
		return """Library(%s, %s)""" % (self.books, self.patrons)
	#computer representation 
	def __repr__(self):
		return str(self)
	#admits patron into the library so that they can check out books 
	def admit_patron(self, patron): #missing one test case on error
		if patron in self.patrons:
			raise DuplicateIdError(patron.patron_id, "Patron")
		self.patrons.append(patron)
		return None
	#searches through patron list for target patrot with his/her id using loop 
	def patron_by_id(self, patron_id):
		#loop through patron list 
		for item in self.patrons:
			if item.patron_id == patron_id:
				return item 
			
		raise MissingIdError(patron_id, "Patron")
	#references target book using its book id raises error if not found 
	def book_by_id(self, book_id):
		#loop through book list 
		for item in self.books:
			if item.book_id == book_id:
				return item
		raise MissingIdError(book_id, "Book")
	#references target book using its title raises error if not found 
	def book_by_title(self, title):
		#loop through book list 
		for item in self.books:
			if item.title == title:
				return item
		raise LookupError('no book found with the title "%s"' % (title))
	#takes target book and appends it to book list 
	def donate_book(self, book):
		#loop through book list 
		if book in self.books:
			raise DuplicateIdError(book.book_id, "Book")
		else:
			self.books.append(book)
		
	#adds book from library list to patron's borrowed
	def loan_book(self, patron_id, book_id):
		
		person = self.patron_by_id(patron_id)
		book_loaned = self.book_by_id(book_id)
		
		if book_loaned in person.borroweds:
			raise DuplicateIdError(book_id, "Book")
		if book_loaned not in self.books:
			raise MissingIdError(book_id, "Book")
			
		person.borroweds.append(book_loaned)
		self.books.remove(book_loaned)
	#adds book from patron's borrowed to library's list 
	def reshelve_book(self, patron_id, book_id):
		person = None
		book = None
		ct2 = 0
		ct = 0
		#loop through patron list 
		for item in self.patrons:
			if item.patron_id == patron_id:
				person = item
				ct2 +=1
		#loop through borrowed list 
		for item1 in person.borroweds:
			if item1.book_id == book_id:
				book = item1
				ct +=1
		if ct2 == 0:
			raise MissingIdError(patron_id,'Patron')
		if ct == 0:
			raise MissingIdError(book_id)
		if book in self.books:
			raise DuplicateIdError(book_id)
		self.books.append(book)
		person.borroweds.remove(book_id)
	#inspect's library book list and displays books that are available 
def display_loanables(library):

	loanables = 'available:\n'
	#loop through library book list 
	for item in library.books:
		loanables += str(item) + '\n'
			
	return loanables 
#finds patron in the library using his/her patron id and displays their 
#checked out books 
def review_checked_out_list(library, patron_id):
	patron_books = ''
	count = 0 
	#loop through library patron list 
	for item in library.patrons:
		if item.patron_id == patron_id:
			count += 1
			if count == 1:
				patron_books += item.name + ':\n'
			for book in item.borroweds:
				patron_books += str(book) + "\n"
			
			return patron_books 
	return ("Patron #%d not found" % (patron_id))
	
	
	
	
		
		
		








	
	
	
	
	
	
	
	
	
	
	
	

		
	
	