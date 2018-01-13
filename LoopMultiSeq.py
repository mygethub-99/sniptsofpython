
#To loop over two or more sequences at the same time, the entries can be paired with the zip() function
#Link to example https://docs.python.org/3/tutorial/datastructures.html

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print('What is your {0}?  It is {1}.'.format(q, a))
