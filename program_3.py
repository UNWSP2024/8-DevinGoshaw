# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).
import random

def main():
    state={'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock','California':'Sacramento','Colorado':'Denver','Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu',
        'Idaho':'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge','Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston',
        'Michigan':'Lansing','Minnesota':'Saint Paul','Mississippi':'Jackson','Missouri':'Jefferson City','Montana':'Helena','Nebraska':'Lincoln','Nevada':'Carson City','New Hampshire':'Concord','New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh','North Dakota':'Bismarck','Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier','Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston','Wisconsin':'Madison','Wyoming':'Cheyenne'
    }
    print('if you want to exit type quit')

    states=list(state.keys())
    random.shuffle(states)

    correct=0
    incorrect=0

    for s in states:
        answer=input('what is the capital of '+ s +'?').strip()

        if answer.lower()=="quit":
            break
        elif answer.lower()==state[s].lower():
            print('correct!')
            correct +=1
        else:
            print('incorrect, the capital of',s,'is',state[s])
            incorrect+=1

    print('Quiz Done')
    print('the number you got correct was:',correct)
    print('the number you got incorrect was:', incorrect)

if __name__=="__main__":
    main()

















