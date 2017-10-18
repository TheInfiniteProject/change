import os
import sys
import time


class main():
	def __init__(self,current):
		self.current = current
	
	def main_method_find_categories(self):
		
		for self.file in os.listdir("FactBookExtract/factbook/fieldsPRINT"):
	

			try:	
				self.current = open("FactBookExtract/factbook/fieldsPRINT/"+ str(self.file),"r")
		
				#print( "---------" + "SUCCESSFUL opening self.file: " + str(self.file) + "---------")
		
		
			except:

				print("ERROR opeining self.file: " + str(self.file))

			search_instance_1.search_file_category_1()
			self.current.close()
			#print(self.current.closed)
	
			if self.current.closed == False:
				print('self.file NOT closed!!! | self.File Status: ',self.current.closed)
				sys.exit()
			else:
				pass

		
		
		for self.file in os.listdir("FactBookExtract/factbook/fieldsPRINT"):
	

			try:	
				self.current = open("FactBookExtract/factbook/fieldsPRINT/"+ str(self.file),"r")
		
				#print( "---------" + "SUCCESSFUL opening self.file: " + str(self.file) + "---------")
		
		
			except:

				print("ERROR opeining self.file: " + str(self.file))

			search_instance_1.search_file_category_2()
			self.current.close()
			#print(self.current.closed)			
	
			if self.current.closed == False:
				print('self.file NOT closed!!! | self.File Status: ',self.current.closed)
				sys.exit()
			else:
				pass




		for ind1, failedFile1 in enumerate(search_instance_1.failed):
			#print(failedFile1, " | Potential Failed File...")
			#time.sleep(3)
			errorFound = True
	

			for ind2, passedFile in enumerate(search_instance_1.passed):
				#print(passedFile, " | Passed File...")

				if failedFile1 == passedFile:
					#print("criteria met...")
					del(search_instance_1.failed[ind1])
					errorFound = False

				if errorFound != False:
					errorFound = True			
			

			if errorFound == True:
				print(failedFile1," | ERROR finding category in this file...")
				sys.exit()
			else:
				#print("Found Category...")
				pass



class create_files():
	def __init__(self):
		pass
	
	def create_category_list_file(self):
		os.system("clear")

		print('\n' * 50)
		print('_________________CATEGORIES_________________')
		print('\n' * 5)
		
		for category1 in search_instance_1.dataType:
			print("".join(category1))		

		category_list_file = open('SORTED_fields_print/category_list_file','w')
		for category2, fileName in zip(search_instance_1.dataType,search_instance_1.passed):
			
			category_list_file.write("".join(category2) + "|" + str(fileName) + "\n")
		
		category_list_file.close()
		print("category_list_file STATUS (True == closed | False == open) : ",category_list_file.closed)


class search_files():
	
	def __init__(self,dataType,catCount,passed,failed,foundCategory):
		
		self.dataType = dataType
		self.catCount = catCount
		self.passed = passed
		self.failed = failed
		self.foundCategory = foundCategory
		


	def search_file_category_1(self):
	
		time.sleep(0.01)

		for line1 in main_instance1.current:			
			
			lineList = []
			holdList = []

			start = 0
			end = 0
			startFlag = 0
			
			self.foundCategory = False
			cont = False
			found = False


			#print("checking line...")

			for char1 in line1:
				lineList.append(char1)

			for index1, char2 in enumerate(lineList):

	
				if char2 == "<" and lineList[index1 + 1] == "/" and lineList[index1 + 2] == "t" and lineList[index1 + 3] == "h"\
				and lineList[index1 + 4] == ">":

					#print('FOUND END...')					
					end = index1

					cont = True
					#print('FOUND CATEGORY..............')
					#time.sleep(2)
		


			for index2, char3 in enumerate(lineList):
		
				if cont == True:

					if char3 == "C" and lineList[index2 + 1] == "o" and lineList[index2 + 2] == "u" and lineList[index2 + 3] == "n"\
					and lineList[index2 + 4] == "t" and lineList[index2 + 5] == "r" and lineList[index2 + 6] == "y" :
						found = True
						#print('country ERROR**************************************')
						#time.sleep(2)

			for index3, char4 in enumerate(lineList):

				if found == False and cont == True:
					if char4 == "<" and lineList[index3 + 1] == "t" and lineList[index3 + 2] == "h":
						startFlag = index3
			
				
					elif char4 == ">" and index3 > startFlag and index3 < end:				
						#print("FOUND START...")
						start = index3 + 2

		
				
				

					limit = end - start


					#print("start: %d" % (start))
					#print("end: %d" % (end))
					#print("%d" % (limit))

					if end != 0 and start != 0:

						for count in range(0,limit):
							holdList.append(lineList[start + count])
						
						self.foundCategory = True
						self.dataType.append(holdList)
						print("".join(self.dataType[self.catCount]))
						self.catCount +=1
						
						self.passed.append(str(main_instance1.file))
					
						break;

		
		if self.foundCategory == False:
			self.failed.append(str(main_instance1.file))
			
	

	def search_file_category_2(self):
		time.sleep(0.01)
		#print('Parsing category names from lines with unfinished <th> tags...')
	
		for index1, line1 in enumerate(main_instance1.current):
			
			
			holdList = []
			lineList = []

			self.foundCategory = False
			foundEnd = False
			foundStart = False
			foundStartIndexEnd = False

			startIndex = 0
			startIndexEnd = 0
		
			for char1 in line1:
				lineList.append(char1)

			for index2, char2 in enumerate(lineList):
				if char2 == "<" and lineList[index2 + 1] == "t" and lineList[index2 + 2] == "h":
					foundStart = True
					startIndex = index2


				if char2 == "<" and lineList[index2 + 1] == "/" and lineList[index2 + 2] == "t" and lineList[index2 + 3] == "h"\
				and lineList[index2 + 4] == ">":
					foundEnd = True
				
				if char2 == ">" and index2 > startIndex:
					startIndexEnd = index2 + 1
					foundStartIndexEnd = True

				if index2 > startIndexEnd and foundStartIndexEnd == True:
					holdList.append(char2)
					
		
		
			
		
			if foundEnd == False and foundStart == True:
				self.foundCategory = True

				for index3, char3 in enumerate(holdList):
					if char3 == '\n':
						del(holdList[index3])

				self.dataType.append(holdList)
				print("".join(self.dataType[self.catCount]))
				self.catCount +=1
				
				self.passed.append(str(main_instance1.file))
			
				break;

		if self.foundCategory == False:
			self.failed.append(str(main_instance1.file))
		

	
			





#create instances of objects

				

search_instance_1 = search_files([],0,[],[],False)					
create_instance_1 = create_files()	
main_instance1 = main(0)




main_instance1.main_method_find_categories()
create_instance_1.create_category_list_file()




				
