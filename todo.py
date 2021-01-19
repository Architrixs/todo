#!/usr/bin/env python
"""
# CoronaSafe Engineering Fellowship Test Problem
# A command-line (CLI) program that lets you manage your todos.
# 21 Dec. 2020 by Architrixs
"""

import sys, os.path
from datetime import date

def todo_help():
	sys.stdout.write("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
""")

def todo_add(item):
	with open('todo.txt', 'a') as file1:
		file1.write(item + '\n')
	sys.stdout.write('Added todo: "'+item+'"\n')

def todo_list():
	if os.path.isfile('todo.txt'):
		with open('todo.txt', 'r') as file1:
			ls=file1.readlines()
			ls=[i.strip() for i in ls]
			for i in range(len(ls),0,-1):
				sys.stdout.write('[{}] {}\n'.format(i,ls[i-1]))
	else:
		sys.stdout.write("There are no pending todos!\n")

def todo_del(num):
	if os.path.isfile('todo.txt'):
		with open('todo.txt', 'r') as file1:
			ls=file1.readlines()
			ls=[i.strip() for i in ls]
			
			if num<=0 or num>len(ls):
				sys.stdout.write("Error: todo #{} does not exist. Nothing deleted.\n".format(num))
			
			else:
				sys.stdout.write("Deleted todo #{}\n".format(num))
				ls.pop(num-1)
				with open('todo.txt', 'w') as file1:
					for item in ls:
						file1.write(item+"\n")
	else:
		sys.stdout.write("Error: todo #{} does not exist. Nothing deleted.\n".format(num))
		
def todo_done(num):
	if os.path.isfile('todo.txt'):
		with open('todo.txt', 'r') as file1:
			ls=file1.readlines()
			ls=[i.strip() for i in ls]
			
			if num<=0 or num>len(ls):
				sys.stdout.write("Error: todo #{} does not exist.\n".format(num))
			
			else:
				done_item= ls.pop(num-1)
				sys.stdout.write("Marked todo #{} as done.\n".format(num))
				with open('done.txt', 'a') as file2:
					file2.write('x '+date.today().strftime('%Y-%m-%d')+' '+done_item + '\n')
				with open('todo.txt', 'w') as file1:
					for item in ls:
						file1.write(item+"\n")

def todo_report():
	with open('done.txt', 'r') as file2:
		done_ls=file2.readlines()
	with open('todo.txt', 'r') as file1:
		ls=file1.readlines()
	sys.stdout.write(date.today().strftime('%Y-%m-%d')+" Pending : {} Completed : {}\n".format(len(ls),len(done_ls)))

def main():
	if len(sys.argv)==1 or sys.argv[1]== 'help':
		todo_help()
		
	elif sys.argv[1]== 'add':
		if len(sys.argv)>2:
			todo_add(sys.argv[2])
		else:
			sys.stdout.write("Error: Missing todo string. Nothing added!\n")
			
	elif sys.argv[1]== 'ls':
		todo_list()
		
	elif sys.argv[1]== 'del':
		if len(sys.argv)>2:
			todo_del(int(sys.argv[2]))
		else:
			sys.stdout.write("Error: Missing NUMBER for deleting todo.\n")
			
	elif sys.argv[1]== 'done':
		if len(sys.argv)>2:
			todo_done(int(sys.argv[2]))
		else:
			sys.stdout.write("Error: Missing NUMBER for marking todo as done.\n")
			
	elif sys.argv[1]== 'report':
		todo_report()
		
	else :
		sys.stdout.write("This command doesn't exist, please refer to this:\n")
		todo_help()
		
if __name__=="__main__": 
    main()
