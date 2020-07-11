import time
import os
print("\t\t\tKBC")
print("1.Play\n2.Score\n3.Exit")
choice=int(input())
score=0
if choice==1:
	name1=str.upper(input("Your Name:"))
	os.system('clear')
	ques=("Name of the first Atomic Submarine of India?","What is the name of first British to visit India? ","Name of the first election commissioner of India?","Name of the first university of India?","Where is India's First nuclear centre?","Name of the first Chinese pilgrim to visit India?", "Name of first foreign recipient of Bharat Ratna?","Where was the first Post Office opened in India?","Name of the first deputy Prime Minister of India?","Name of first Space Tourist of India?","Name of the first Aircraft Carrier Indian Ship?","Name of First Indian who reached south pole?","Name of first Indian who won Billiards Trophy?","Name of the First Indian Prime Minister who resigned from Office?","First Indian recipient of Oscar Award?","Name of the first Indian President to Die in office?","Name of the First Indian Author to get the Anderson Award?","Name of First Indian Missile?","Name of first Indian Pilot?","Name of the first Chief of Naval staff of India?","Name of the first Indian to win Magsaysay Award?","Name of first Indian to win Nobel Prize?","First Scientist of India to get Nobel Prize in Economics?","Name of the First Indian Submarine?","Name of the first person to get Paramvir Chakra?","First Indian to go into space?","Name of first Indian to get Bharat Ratna Award?","Name of first speaker of Lok Sabha?","Name of first president of Indian National Congress ?","First President of India ?")
	print("1.Level 1\n2.Level 2\n3.Level 3")
	level=int(input("Choose any level:"))
	os.system('clear')
	if choice==2:
		tyu=open("kbc123.txt","rt")
		me=tyu.read()
		print(me)
		tyu.close()
		input()
		
	elif level==1:
				print(ques[0])
				print("1.I.N.S Chakra\t2.Arihant\n3.Akula 2\t4.Shisumar")
				opt=int(input("Choose your answer:"))
				if opt==1:
										print("Correct")
										score=score+1000
				else :
										print("Wrong")
										score=score-1000
				time.sleep(1)
				os.system('clear')
				
				
										
				print(ques[1])
				print("1.John\t2.George Bush\n3.Hawkins\t4.Lord Hamilton")
				opt=int(input("Choose your answer:"))
				if opt==3:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[2])
				print("1.Sunil Arora\t2.Sukumar Sen\n3.Ashok Lavasa\t4.Sushil Chandra")
				opt=int(input("Choose your answer:"))
				if opt==2:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[3])
				
				print("1.Takshila University\t2.Nalanda University\n3.Banaras University\t4.Bharat University")
				opt=int(input("Choose your answer:"))
				if opt==2:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[4])
				print("1.Jaipur\t2.Rampur\n3.Mayapur\t4.Tarapur")
				opt=int(input("Choose your answer:"))
				if opt==4:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[5])
				print("1.Sun chi\t2.Fa Wien\n3.Xi Ping\t4.Chen Hung")
				opt=int(input("Choose your answer:"))
				if opt==2:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[6])
				
				print("1.Khan Abdul Gaffar Khan\t2.V.R.Gill\n3.Ram Gopal\t4.Wilson Jones")
				opt=int(input("Choose your answer:"))
				if opt==1:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[7])
				print("1.Ranchi in 1727\t2.Kolkata in 1727\n3.Delhi in 1727\t4.Lucknow in 1727")
				opt=int(input("Choose your answer:"))
				if opt==2:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[8])
				print("1.Jawaharlal Nehru\t2.Motilal Nehru\n3.Shubhash Chandra Bose\t4.Sardar Vallab Bhai Patel")
				opt=int(input("Choose your answer:"))
				if opt==4:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				time.sleep(1)
				os.system('clear')
				print(ques[9])
				print("1.Rakesh Sharma\t2.Sunita Williams\n3.Wilson Paul\t4.Santosh George")
				opt=int(input("Choose your answer:"))
				if opt==4:
													print("Correct")
													score=score+1000
				else :
													print("Wrong")
													score=score-1000
				
				time.sleep(1)
				print(f"Your total score is {score}")
				qwer=open("kbc123.txt","a")
				qwer.write(f"{name1} : {score}\n")
				qwer.close()
	elif level==2:
		print(ques[10])
		print("1.Sukhoi\t2.I.N.S Vikrant\n3.HAL Tejas\t4.SEPECAT")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[11])
		print("1.R.N.Shukla\t2.D.B. Mahawar\n3.Col. IK Bajaj\t4.V.R.Gill")
		opt=int(input("Choose your answer:"))
		if opt==3:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[12])
		print("1.Wilson Jones\t2.Amartya Sen\n3. RD Katar \t4.Roman ")
		opt=int(input("Choose your answer:"))
		if opt==1:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[13])
		print("1.Indira Gandhi\t2.Morari Desai\nRajiv Gandhi\t4.J.R. Nehru")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[14])
		print("1.R.N. Shukla\t2.Bhanu Athaiya\n3.Ruskin Bond\t4.G.R. Bhosle")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[15])
		print("1.Pranav Mukhrjee\t2.Dr. Jakir Hussain\n3.Gyan Jail Singh\t4.Dr. Rajendra Prasad")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[16])
		print("1.Harivansh Rai\t2.LaxmiNaryan Mehata\n3.Ruskin Bond\t4.Jai Chand")
		opt=int(input("Choose your answer:"))
		if opt==3:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')

		print(ques[17])
		print("1.Sukhoi\t2.HAL Tejas\n3.Spuntunik\t4.Prithvi")
		opt=int(input("Choose your answer:"))
		if opt==4:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[18])
		print("1.J.R.D Tata\t2.Seth Shiv Narayana Birla\n3.Dhirubhai Ambhani\t4.Lakshmi Mittal")
		opt=int(input("Choose your answer:"))
		if opt==1:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[19])
		print("1.Vice Admiral SV Bhokale\t2.Vice Admiral Satish Namdeo Ghormade\n3.Vice Admiral R.D. Khatar\t4.Vice Admiral Ravindra Jayant")
		opt=int(input("Choose your answer:"))
		if opt==3:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print("Your total score is : ",score)
		qwer=open("kbc123.txt","a")
		qwer.write(f"{name1} : {score}\n")
		qwer.close()
	elif level==3:
		print(ques[20])
		print("1.Acharya Vinoba Bhave\t2.C.V Raman\n3.Satendranath Bose\t4.Srinivasa Ramaanujan")
		opt=int(input("Choose your answer:"))
		if opt==1:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[21])
		print("1.Mother Teresa\t2.Kailash Satyarthi\n3.Ravindranath Tagore\t4.Har Gobind Khorana")
		opt=int(input("Choose your answer:"))
		if opt==3:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		
		os.system('clear')
		print(ques[22])
		print("1.Dr. S Krishnan\t2.Dr. Amartya Sen\n3.Dr. Rakesh Singh\t4.Dr. Kaveri")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[23])
		print("1.Major Hosiar Singh\t2.I.N.S Chhaveri\n3.Lance Naik Albert\t4.Flying officer Navjot Singh")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[24])
		print("1.Major Shaitan Singh\t2.Major Rajendra Singh\n3.Major Suresh Rawat\t4.Major Somath Singh")
		opt=int(input("Choose your answer:"))
		if opt==4:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[25])
		print("1.Sqn. Ldr. Rakesh Sharma\t2.Sunita Williams\n3.Kalpana Chawla\t4.Ravish Malhotra")
		opt=int(input("Choose your answer:"))
		if opt==1:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[26])
		print("1.Pranav Mukhrjee\t2.Gyan Jail Singh\n3.Rajendra Prasad\t4.Dr. S Radhakrishnan")
		opt=int(input("Choose your answer:"))
		if opt==4:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[27])
		print("1.Om Birla\t2.M.A. Ayyangar\n3.G.V. Mavlankar\t4.Ganesh Vasudhar")
		opt=int(input("Choose your answer:"))
		if opt==3:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		os.system('clear')
		print(ques[28])
		print("1.Sonia Gandhi\t2.W.C. Banerjee\n3.Dadabhai Naroji\t4.Badruddin Tyabji")
		opt=int(input("Choose your answer:"))
		if opt==2:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		
		os.system('clear')
		print(ques[29])
		print("1. Dr. Rajendra Prasad\t2.Dr. S Krishnan\n3.Dr. Zakir Hussain\t4.Pranav Mukhrjee")
		opt=int(input("Choose your answer:"))
		if opt==1:
			print("Correct")
			score=score+1000
		else :
			print("Wrong")
			score=score-1000
		time.sleep(1)
		print("Your total score is : ",score)
		qwer=open("kbc123.txt","a")
		qwer.write(f"{name1} : {score}\n")
		qwer.close()

	elif choice==3:
		exit()
	