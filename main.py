from random import choice

answers = ['Very doubtful', 'Outlook not so good', 'My sources say no', 'My reply is no', 'Don’t count on it',
           'Concentrate and ask again', 'Cannot predict now', 'Better not tell you now', 'Ask again later',
           'Reply hazy, try again', 'Yes', 'Signs point to yes', 'Outlook good', 'Most likely', 'As I see it, yes',
           'You may rely on it', 'Yes — definitely', 'Without a doubt', 'It is decidedly so', 'It is certain']
print('Hello world, i am a magic ball, and i know an answer to your any question')
name = input("What's your name?")
print(f'Hello, {name}')
asking = True
while asking:
    question = input('Ask your question: ')
    print(choice(answers))
    response = input('Do you want to ask another question? (y/n)')
    if response.lower() == 'n':
        asking = False
        print('Come back if you have more questions.')
