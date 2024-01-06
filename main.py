print ('Welcome to Elite 101!')
name = input('What is your name?:')
age = input(name+ ' is a cool name. How old are you?:')
print('How may I help you today ' + name)
print()
print('Choose from the following options:')
print('1.Ask for an intresting fact')
print('2.Ask for a funny joke')
print('3.Ask about the chatbot')
print('4.Exit the conversation')
options = input('Enter your choice:')
if(options == '1'):
  print('Clouds weigh up to one million pounds!')

elif(options == '2'):
  print('What do you call a cow witout legs? Ground beef!')

if(options == '3'):
  print('I am the Elite 101 PreWork Chatbot. I was created by Adedayo Raifu.')

else:
  print('Bye ' + name + ' have a great day!')


