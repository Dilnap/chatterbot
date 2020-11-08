import time
from pip._vendor.distlib.compat import raw_input
a = 'Awesome. Let’s fix a time for you to see the demo ✨'
b="Alright. Talk soon, bye now 👋"
email=[]
dt=[]
d={}
z=0
e=None
def insent():
    print( "By integrating with your marketing automation and CRM platforms,  Insent  identifies the browsing accounts before they fill your form")
    print("If the account is a good fit and is ready for a conversation , Insent will alert the right "
          "SDRs/AEs and enable them to send a contextual, real-time message. ")
    print("Would you like to see a live demo? 💻")
    print("1.absolutely")
    print("2.not now,thanks")
    m = input("enter:")
    if m == '1':
        demo()
    else:
        print(b)
        time.sleep(10)
        z = input("enter 1 for restart conversation")
        if (z == '1'):
            restart()
def demo():
    print(a)
    x = input("Enter the date and time in the format d/m/y h:m(am/pm):")
    dt.append(x)
    print(b)
    time.sleep(10)
    z = input("enter 1 for restart conversation")
    if (z == '1'):
        restart()
def expert():
        print("Let me try to see if the team is available at the moment ")
        time.sleep(10)
        print("Looks like our agents aren’t available at the moment. But I’m sure they are excited to speak with you.  ")
        print("May I have a good email for you?")
        global e
        e = raw_input("Enter email in the format xyz@abc.com:")
        email.append(e)
        print("Do you want to pick a time for a demo without waiting? ")
        print("1.That'd be great")
        print("2.not now")
        x = input("enter:")
        if x == '1':
            demo()
        elif x == '2':
            print(b)
            time.sleep(10)
        z = input("enter 1 for restart conversation")
        if (z == '1'):
            restart()
def restart():
    print("You're back again,Awesome..Ready to see insent demo?")
    print("Lets do it,choose the bst way for you")
    print("1.yes tell me more about insent now")
    print("2.show me a demo")
    print("3.speak with a conversational marketing expert")
    print("4.just browsing")
    n = input("enter the choice:")
    if n == '1':
        insent()
    elif n == '2':
        demo()
    elif n == '3':
        if (e):
            print("you already fix a time for meeting:")
            print("Do you want to change it?")
            y = input("enter y or n")
            if (y == 'y'):
                x = input("Enter the date and time in the format d/m/y h:m (am/pm):")
                d[e] = x
                print(b)
                z = input("enter 1 for restart conversation")
                if (z == '1'):
                    restart()
            elif y == 'n':
                print(b)
                z = input("enter 1 for restart conversation")
                if (z == '1'):
                    restart()
        else:
           expert()
    else:
        print(b)
        time.sleep(10)
        z = input("enter 1 for restart conversation")
        if (z == '1'):
            restart()
print("Lets do it,choose the bst way for you")
print("1.yes tell me more about insent now")
print("2.show me a demo")
print("3.speak with a conversational marketing expert")
print("4.just browsing")
n = input("enter the choice:")
if n == '1':
    insent()
elif n == '2':
    demo()
elif n == '3':
    expert()
else:
    print(b)
    time.sleep(10)
    z=input("enter 1 for restart conversation")
    if(z=='1'):
        restart()
