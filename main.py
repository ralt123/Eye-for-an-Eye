# Notes

# Functions will allow the user to return to previous story points
# Another test

import textwrap
import time
global globaldict
# Dictionary to contain necessary variables - test
globaldict = {"albertInfo": "0","virus":"0","sattempt":3,"ddos":"0","datab":"0","deleted":"0","spammed":"0","friendly":"0","food":"0","reported":"0","vpnGermany":"0","vpnLondon":"0","vpnAlbert":"0","question1":"0","question2":"0","question3":"0"}
runSection="Start"

# Prints the text to screen 
def textPrint(toPrint):
    # Controls when the text wraps to the next line as to prevent mid word text wrapping
    print(textwrap.fill(toPrint, 80))
    print("")

# Two empty lines around the input for better formatting
def spacedInput(outputText):
    print("")
    nextPart = input("Selection - ")
    print("")
    return nextPart

# Template choiceMaker(["1","Run away","runAway"])
# Outputs "Run away - 1"
# If the user inputs "1" then the function "runAway" is ran
# Provides the user with choices
def choiceMaker(choicesList):
    while True:
        for i in choicesList:
            if len(i)==1:
                tempNum=i
            elif (choicesList.index(i)+1)%3==0:
                continue
            else:
                print(tempNum + " - " + i)
        selection=spacedInput("Selection - ")
        if selection in choicesList and len(selection)==1:
          return choicesList[choicesList.index(selection)+2]
        else:
          print("Please enter a valid input")
        
# Story points
def Start():
    textPrint("Earlier on today, I asked my best friend ‘Dani’ for his Netflix account details, since I've been having some financial problems. I was annoyed with his selfish response; he wanted me to “ask someone else as he and his family were using so he didn’t want me to watch my shows that could cause the Netflix algorithm to give him weird recommendations and his family would think it was him who watched it instead”. I replied:\n")
    return choiceMaker(["1","Okay","okay","2","No, I thought we were friends","noWeAreFriends","3","for testing","choice1"])

def noWeAreFriends():
    textPrint("He replied, \"I don't care what you think but i am not giving it to you\".")
    print("I thought, \"How could you do this to me\"\n")
    return choiceMaker(["1","Continue","okay"])
    
def okay():
    textPrint("Obviously, I did understand his reasoning as systems like Netflix are based on machine learning that rewrite themselves as they learn from their own users. Every time you press play and spend some time watching a TV show or a movie, Netflix is collecting data that informs the algorithm and refreshes it. The more you watch the more up to date the algorithm is and so if I watched anything on his account, the system would refresh and recommend him shows that are not his taste and this can be annoying.")
    return choiceMaker(["1","Continue","next"])

def next():
    textPrint("However, this made me livid as he knows that I just lost my job because I got caught trying to hack into the finance database using a SQL injection to add more money to my salary. The SQL injection was easy to perform as all I had to do was go to the site which shows how much we are getting paid for each tasks we have done and how long we have worked for; I then wrote code instead of my username to trick the program to execute my username as a code, which got me admin access to change the values in the database. However, I didn’t expect that there was a camera in the finance office which caught me as I was messing with the computer and was fired then and there. I expected:")
    return choiceMaker(["1","Some empathy from someone who I call my ‘best friend’","someEmpathy","2","That he would never help me","neverHelp"])

def someEmpathy():
    textPrint("As we are both computer science students and have benn friend for 5 years. There fore i decided that the only suitable thing to do, would be to take revenge by a cyber-attack. As it would test his abilities as a computer scientist and allow for me to have some petty revenge.")
    return choiceMaker(["1","Continue","Revengeplan"])

def neverHelp():
    textPrint("I knew he would never help me even though I have look after him and stuck with him for so long so I've decide to forget about him and move on with my  life and never contact him again.")
    return choiceMaker(["1","Go back","next"])

def Revengeplan():
  textPrint("I initially decided on three potential ways and techniques that I could implement. A smishing text (SMS), phishing email or keylogger are some of the various ways that I could’ve used to get back at his and test his skills in cyber security. I decided on:")
  return choiceMaker(["1","A smishing text","Asmishingtext","2","Phishing email","Phishingemail","3","Keylogger","keylogger","4","Forgetting about it and going on with my life","Forgetaboutit"]) 

def Asmishingtext():
  textPrint("A smishing text is relatively easy to create as I already have his number and personal details. The definition of SMS phishing is “the act of committing text message fraud to try to lure victims into revealing account information or installing malware.” It is essentially a type of phishing which uses a SMS text message as its basis. All I need to do is make a simple text message, pretending to be Netflix, asking to update his account and card details for extra security. If he doesn’t notice any signs that signify the text message is fraudulent then he will likely provide his account details. However, this technique was useless as he and I have already done this many times to other people and it’s always hilarious when the other person starts madly reply to give his money back and that he would call the police, which would have done nothing as we sent it from a one-time number that belonged to no one. Therefore, this would be ineffective against him and he would easily recognise it and not open the link. Therefore this was ineffective and you decided on:")
  return choiceMaker(["1","Phising email","Phishingemail","2","Keylogger","keylogger"])

def Phishingemail():
  textPrint("A phishing email is practically identical to SMS phishing, but uses email as its basis- rather than text. It would allow me to gain access to Dani’s account details in the same way because I am essentially doing the same thing; impersonating Netflix and asking him to update his account information for security purposes.")
  return choiceMaker(["1","Contiue","phising2"])

def keylogger():
  textPrint("A keylogger is another technique that I contemplated on using. It is a computer program that logs keystrokes from the victim computer system, with the user being unaware that they're being ‘monitored’. In order to gain access to private information, such as account details and passwords. If I were to utilise a keylogger to obtain Dani’s account details, then I would need physical access to his computer system. It would involve me, unzipping and installing the content from the keylogger (via USB) and returning later when I am ready to go through all his keystroke data. However, this would end up being a long-winded process, as I would need to install the keylogger covertly and be left with a large file of keystrokes to analyse. However, I would not even be able to do the first step as I haven’t met him in years, and I wasn’t about to meet him for just a Netflix account. Therefore, I decided on not using it as my tool of justice. Therefore this was inefective so i decided on:")
  return choiceMaker(["1","Phising email","Phishingemail","2","A smishing text","Asmishingtext"])

def Forgetaboutit():
  textPrint("I thought that instead of being petty, I could accept that it was ultimately his choice whether or not he decided to share his account with me. I realise that I should change as a person overall. I could either")
  return choiceMaker(["1","Turn over a new leaf","newleaf","2","Not change","notchange"])

def newleaf():
  textPrint("I thought about how i could reply to Dani and apologise for acting the way I have. But that's a lot of work, i essentially get nothing out of it and ultimately results in Dani getting away with what he has done to me. I need justice.")
  return choiceMaker(["1","Continue","continue1"])

def notchange():
  textPrint("I realised that changing was simply not me, and that Dani had to pay for what he has done to me. I returned to")
  return choiceMaker(["1","Revenge plan","Revengeplan"])

def continue1():
  textPrint("I opened the messages that Dani had sent me, i never bothered to read them, he saw that I was ignoring him and in one message he wrote \"You realise that you're being petty, it is your fault that you lost your job, and my choice to share my account. Just grow up and realise not everything will go your way.\"\n")
  return choiceMaker(["1","That did not sit right with me","notsightright"])

def notsightright():
  textPrint("That message further solidified the fact that he knows what he is doing to me, it is only a Netflix account and i've known him for years. He is selfish, needs to be taught a lesson and I need my justice. I tried to change but it's time to return to my")
  return choiceMaker(["1","Revenge plan","Revengeplan"])

  
def phising2():
  textPrint("I had to take two main steps to ensure he didn’t recognise it as a fraudulent email.")
  return choiceMaker(["1","Step 1","step1"])

def step1():
  textPrint("The email I use would’ve had to seem as trustworthy as possible as well as looking as closely to the genuine Netflix email as possible. Knowing Dani he will notice it isn't exact as he's always been the type to analyse everything and anything that enters his life. I remember this one time")
  return choiceMaker(["1","Relive that \"one time\"","oneTime","2","Step 2","step2"])

def oneTime():
  textPrint("Dani and I were going to a resturant after a lecture, we were talking and having a very good conversation, and then all of a sudden a small child came sprinting up and down past our table, over and over again. As anyone would i began to get quite annoyed and in my eyes i had two options:")
  return choiceMaker(["1","leave the child be and get more and more annoyed","Moreannoyed","2","get the child to stop and continue our conversation","Stopchild"])
def Moreannoyed():
  textPrint("I did not choose this option, why would I? why can't parents be more responsible with their child so i'm not forced to act. What I did was justice for me and Dani.")
  return choiceMaker(["1","Back to the story","oneTime"])

def Stopchild():
  textPrint("When the kid came to run back past our table I stook my foot out, he didn't see it and ran straight into it, he practically did a flip, then skidded across the floor. The kid looked back at me with tears in his eyes and I just looked back at Dani to")
  return choiceMaker(["1","continue our conversation.","continue2"])

def continue2():
  textPrint("Instead of continuing to talk Dani gave me this... look, he squinted his eyes at me, furrowed his brow and raised the corners of his mouth as if to say \"why would you do that\" He then got out of his chair to help that demon of a kid (who was now of course crying) up, he said he was \"sorry for my friend\" and walked him back to his neglectful parents. As if it was my fault. After that he sat down and told me that he didn't feel like eating, and left. We stayed friends but I know after that moment something in our friendship changed. I know he was psychoanalysing me before and now he thought I was some kind of psychopath. What I did was completely justified but Dani being Dani, could not see that.")
  return choiceMaker(["1","Step 1","step1"])

def step2():
  # print instead of "textPrint" due to formatting concerns
  print("Subject: NETFLIX: Security verification required.\n\nNETFLIX \n\nHi dear, \n\nWe have detected suspicious activity within your account. \n\nThere have been many log-in attempts linked to this Netflix emails. So, for extra security, we are requiring all users with these problems to verify their account information. \n\nPlease follow the instructions in the link below. All the \n\nsteps provided are to ensure the security of your account \n\n-Your friends at Netflix \n\nUPDATE YOUR DETAILS\n\nxxx\n\nQuestions? Call 1-234-567-890\n\nG32 Armstrong Siddeley Building, Gosford Street, CV1 5PY, U.K. \n\nUnsubscribe | Terms of Use | Privacy | Help Centre\n\nThis message was mailed to Dani4006@gmail.com by Netflix because you are a former Netflix member. \n\nSRC: 00876 en GB\n")
  return choiceMaker(["1","Dani's Perspective","daniPOV"])

def daniPOV():
  textPrint("I received an[email|Step 2 from ‘Netflix’ today, asking me to update my account details for extra security. Because there has supposedly been a suspicious number of log-in attempts made. Which I thought was odd; I don’t share my account details with anyone.\n\nThe only way this could be possible is if someone in my family was sharing our account with their friends")
  return choiceMaker(["1","Continue","sisterStory"])

def sisterStory():
  textPrint("My little sister Maria has asked me in the past if she could share the account with her friend, I specifically told her no, and not to do it. I even monitored my emails for unknown logins from another location but it never happened. So this doesn't make sense.\nBefore considering that option I decided to look closer a the email instead")
  return choiceMaker(["1","Inspect email","emailInspection"])

def emailInspection():
  textPrint("I noticed that the structure of this email seemed off... there were various signs that lead me to conclude that this email had to be fake, and most likely a phishing attempt. ")
  return choiceMaker(["1","Continue","emailInspection2"])

def emailInspection2():
  textPrint("I checked if the email was sent from a public email domain. I compared this email address to past email I received from Netflix, in which the domain name was @Netflix.com.\n\nThis immediately indicated that the email I received today was indeed a phishing email, because it did not have a public domain, instead it had a private domain. No legitimate company in the world would use this, especially a big corporation like Netflix. Therefore, this RedFlag 100% guaranteed that this was not a genuine email from Netflix.")
  return choiceMaker(["1","Play the ‘game’ and respond with a taste of his own medicine","ddos1","2","Don't take revenge","forgiveness"])

def forgiveness():
  textPrint("I decided not to take revenge as I know that your friend just lost his job and was in greicing so I'll let him of easy. The end.")
  return choiceMaker(["1","Go back","emailInspection2"])

def ddos1():
  textPrint("A DDoS attack typically involves infected nodes from different networks attacking the same victim simultaneously.\nDue to all the incoming flooding traffic originating from different networks, it’s impossible to stop the attack by simply using ingress filtering, the attack renders the target machine unable to access any desired server; all the necessary traffic to access the server are unable to processed by the client due to the large amount of useless incoming requests sent by the “zombies” taking a considerable amount of time to process.")
  return choiceMaker(["1","How does it work?","ddos2","2","Don't care, skip","choice1"])

def ddos2():
  textPrint("The simplest way to describe how a DDoS attack works is by comparing it to highway traffic. Let’s say that the request from target machine is a red car, the internet is the highway road, and each of those many requests from “zombie” machines are individual black cars.")
  return choiceMaker(["1","Go on...","Go_on"])

def Go_on():
  textPrint("If the target machine wants to communicate with a server via the internet, it would have to first send a request to the server, and that request is demonstrated by the red car. The red car needs to drive to the server as to deliver the user’s request, and to reach this destination the red car must drive through the highway, of which resembles the internet. As a DDoS attack is essentially just sending lots of useless requests to flood the victim, of which must sent through internet as well, this would mean that the black cars would flood the highway, which would cause an extreme traffic jam due to those black cars having to be slowly processed by the victim; the black cars would block the red car’s route, which results in the red car in being unable to reach the destination, therefore the request from the target machine is unable to reach the server, or may take large amount of time to reach as the red car must slowly wait for the black cars to move as to reach its destination.")
  return choiceMaker(["1","Seems difficult","Seemsdifficult"])

def Seemsdifficult():
  textPrint("Instead of spending my time infecting innocent victims to force them to fulfil my commands, I could simply utilize data breaches for my revenge. Data breaches vary, but usually contain useful personal information, if Albert’s personal information is revealed within the breach, I could use against it him. All I require is a unique piece of information to identify Albert’s personal information in the extensive list of breached information at my disposal.")
  return choiceMaker(["1","How will I identify which data belongs to Albert?","IdentifyAlbert"])

def IdentifyAlbert():
  textPrint("Luckily, I know one of Albert’s personal emails in addition to his full name, this should be sufficient as to allow me to identify him. While public access to breached data may be limited, the available data should be sufficient for my cause. The breached data could potentially reveal the plaintext password he has used in the past or other emails owned by him of which I am unaware of, which I could utilize.")
  return choiceMaker(["1","What good will this do?","Whatgood"])

def Whatgood():
  textPrint("I will use the combination of his leaked emails and passwords to attempt to sign into various services in hopes of successfully logging into his account as to steal it by changing its associated email to a personal throwaway email and its password to one only known by myself. If I’m lucky, I may even gain access to one of his emails.")
  return choiceMaker(["1","What about security measures?","Securitymeasures"])
  
def Securitymeasures():
  textPrint("Whilst attempting to log into various services by using his details, I may consider using a VPN. Not only would this allow me hide the fact that I’m the one attacking Albert, but also allow my IP to be geographically closer to Albert, as to prevent digital security measures from flagging my login attempt as being malicious due to the geographical difference between Albert and I. However, as my IP would still be different from Albert’s, my login attempt may be blocked. Whilst I would ideally like to have the same IP as Albert as to make it appear that Albert is logging in from his usual location and IP, it would require me to gain access to Albert’s network which would be far too difficult due to Albert’s computing knowledge preventing me from directly infecting him.")
  return choiceMaker(["1","What if his accounts are too secure?","Secureaccount"])
  
def Secureaccount():
  textPrint("If I’m unable to successfully login to a service using his details, I could resort to flooding his emails with spam. Similarly, to a DDOS attack, this would prevent Albert from viewing the useful emails he has received as his inbox would be flooded with a large amount of worthless emails. Although, this method would not be perfect due to anti-spam measures in modern emails, furthermore, there is no guarantee that I even find Albert’s information in a data breach which would render my plan worthless.")
  return choiceMaker(["1","Time to make a choice","choice1"])

def choice1():
  return choiceMaker(["1","Prepare to DDOS attack Albert","choiceDDOS","2","Search data breaches","choiceData","3","End the story","endingCheck"])

def choiceDDOS():
  textPrint("I'll have to create a botnet before starting the DDOS attack")
  return choiceMaker(["1","Create botnet","botnet","2","Go back","choice1"])

def botnet():
  textPrint("This is way too difficult for me, not to mention extremely overkill.\nAlbert only sent me a malicious email, there's no need for me to call upon an army of zombies for revenge")
  globaldict["ddos"] = "1"
  return choiceMaker(["1","Reconsider","choice1"])

def choiceData():
  textPrint("Various promising websites appear before you.") #this is where i left
  if globaldict["virus"]=="1":
    textPrint("I'm not touching that virus again.")
    return choiceMaker(["1","Cached version of Albert's old social media page","socialMedia1","2","Data breach from 2 years ago","dataBreach"])
  else:
    return choiceMaker(["1","passwordHacker.exe","virus1","2","Cached version of Albert's old social media page","socialMedia1","3","Data breach from 2 years ago","dataBreach"])

def socialMedia1():
  textPrint("I have discovered Albert's old social media page.")
  return choiceMaker(["1","View friends","socialFriends","2","View interests","socialInterests","3","View details","socialDetails","4","Harass Albert","socialHarass","5","Report Albert's posts","socialReport","6","Review choices","choice1"])

def socialFriends():
  if globaldict["virus"]=="1":
    print("Fr1en&s # \n-5ac3b Matth5ws\n-Iris S&er#ey \n-Zorana *egi$e \n-Si&fra*Fred\n#3 others *idden")
  else:
    print("Friends - \nJacob Matthews\nIris Sherley \nZorana Regine \nSiofra Fred \n13 others hidden\n")
  textPrint("I don't use social media so it's no surprise that I'm not listed")
  return choiceMaker(["1","Go back","socialMedia1"])

def socialInterests():
  if globaldict["virus"]=="1":
    print("3avo*ite$Hobb#: Pro*ra1min5\n-Favo5rite fo$d:#Chicken\n-*avouri5e Mo1ie3 The *od5athe%\n-Favourite3Music Genre: Undecid&d\n-1avo#uit5 Drink: Pep%i")
  else:
    print("Favorite Hobby: Programming\nFavourite food: Chicken\nFavourite Movie: The Godfather\nFavourite Music Genre: Undecided\nFavoruite Drink: Pepsi\n")
  if globaldict["food"]=="1":
    textPrint("Am I missing something?")
  else:
    textPrint("Nothing of interest...")
  return choiceMaker(["1","Go back","socialMedia1"])

def socialDetails():
  if globaldict["virus"]=="1":
    textPrint("His #rivacy setti5gs 3akes t5is5page essential*y *sele%s")
  else:
    textPrint("His privacy settings makes this page essentially useless.")
  return choiceMaker(["1","Go back","socialMedia1"])

def socialHarass():
  textPrint("I could make multiple accounts and virutally harass him for revenge.")
  return choiceMaker(["1","Start making accounts to harass him","socialHarass2","2","Reconsider","socialMedia1"])

def socialHarass2():
  textPrint("After some consideration, harassing him doesn't seem to be a befitting revenge. It's cyber crime vs cyber crime, eye for an eye, I don't want ot make it too personal.")
  return choiceMaker(["1","Go back","socialMedia1"])
  
def socialReport():
  textPrint("I mindlessly reported over a hundred posts, it's unlikely to have any impact considering I'm viewing the cached version, but it was enjoyable.")
  globaldict["reported"]="1"
  return choiceMaker(["1","Go back","socialMedia1"])
  
def virus1():
  textPrint("I attempted to download the exe file but my antivirus prevented me from doing so.")
  return choiceMaker(["1","Go back","choice1","2","Proceed to download file","virus2"])
  
def virus2():
  textPrint("The exe file makes me feel uneasy.")
  return choiceMaker(["1","Delete it","choice1","2","Run the .exe file","virus3"])

def virus3():
  textPrint("Windows smartscreen prevents the file from running.")
  return choiceMaker(["1","Delete the file","choice1","2","Run anyway","virus4"])

def virus4():
  textPrint("5 ran t$e .exe 3ile, it*doe#nt#app5ar $o do a1ythi*g impor%ant.")
  globaldict["virus"]="1"
  return choiceMaker(["1","What's going on?","virus5"])

def virus5():
  textPrint("The virus appears to corrupt certain peices of text on my pc.\n&t le5st * can stil# use m* 3c for reve#ge")
  return choiceMaker(["1","Review choices","choice1"])

def endingCheck():
  return choiceMaker(["1","End","ending","2","Go back","choice1"])

def dataBreach():
  textPrint("You find various emails and password related to Albert, all of which are years old. Furthermore, you note down his IP - 26.49.210.85")
  return choiceMaker(["1","Spend hours attempting to log into different services","service1","2","Flood his emails with spam","spamemail","3","Warn him about his data being leaked","dataleak","4","Review choices","choice1"])

def service1(): #yo harry where did you get this from
  textPrint("After 30 minutes I've find a success combination for a service.\nIt's for a gaming website, but whenever I attempt to login, I get blocked due to my location not matching Albert's.")
  return choiceMaker(["1","Pull out the VPN","vpn1","2","Try Albert's details on other services","service2"])

def vpn1():
  if globaldict["vpnAlbert"]=="1" and globaldict["vpnGermany"] == "1" and globaldict["vpnLondon"]=="1":
    textPrint("This VPN is worthless, what a waste of time...")
  textPrint("What should I set my location to?")
  return choiceMaker(["1","London","vpnLondon","2","Germany","vpnGermany","3","Use Albert's IP","vpnAlbert","4","Go back","service1"])

def vpnLondon():
  textPrint("Still blocked...")
  globaldict["vpnLondon"]="1"
  return choiceMaker(["1","Go back","vpn1"])

def vpnGermany():
  textPrint("Still blocked...")
  globaldict["vpnGermany"]="1"
  return choiceMaker(["1","Go back","vpn1"]) 

def service2():
  textPrint("I was mere minutes away from giving up and going to sleep, but then I found another service that I could sign into using Albert's details.\n\nI don't have the energy to search for more services, I'm hoping this will work...")
  if globaldict["datab"]=="0":
    return choiceMaker(["1","Log in","serviceLogin"])
  else:
    return choiceMaker(["1","Log in","codeSite1"])

def serviceLogin():
  textPrint("Security question:\nAttempts remaining - " + str(globaldict["sattempt"]) + "/3\nRemaining Questions - 3/3\n\nSecurity questions, I'm assuming I have to answer them because my IP doesn't match Albert's")
  if globaldict["sattempt"]==0:
    textPrint("Check email for account recovery.\nI'm locked out")
    return choiceMaker(["1","Use a VPN","vpnBlocked","2","Review choices","choice1"])
  else:
    return choiceMaker(["1","Security question 1","question1","2","Use a VPN","vpnBlocked","3","Review choices","choice1"])
    
def vpnBlocked():
  textPrint("I'm now no longer able to access the website, regardless of my location.\nThe service somehow knows i'm using a VPN...")
  return choiceMaker(["1","Disable VPN","serviceLogin"])
  
def question1():
  if globaldict["sattempt"]==0:
    textPrint("No more attempts...")
    return choiceMaker(["1","Review choices","choice1"])
  else:
    if (input("Enter your first name: ")).lower() == "albert":
      globaldict["question1"]="1"
      textPrint("Two more to go...")
      return choiceMaker(["1","Next question","question2"])
    else:
      globaldict["sattempt"]=globaldict["sattempt"]-1
      textPrint("Inorrect - " + str(globaldict["sattempt"]) + " attempts remain.")
      return choiceMaker(["1","Try again","question1","2","Cancel login attempt","serviceLogin"])
      
def question2():
  if globaldict["sattempt"]==0:
    textPrint("No more attempts...")
    return choiceMaker(["1","Review choices","choice1"])
  else:
    if (input("Enter your favourite food: ")).lower() == "chicken":
      globaldict["question2"]="1"
      textPrint("Only one more to go.")
      return choiceMaker(["1","Next question","question3"])
    else:
      globaldict["sattempt"]=globaldict["sattempt"]-1
      textPrint("Inorrect - " + str(globaldict["sattempt"]) + " attempts remain.")
      return choiceMaker(["1","Try again","question2","2","Cancel login attempt","serviceLogin"])
  
def question3():
  if globaldict["sattempt"]==0:
    textPrint("No more attempts...")
    return choiceMaker(["1","Review choices","choice1"])
  else:
    if (input("Enter your best friends first name: ")).lower() == "dani":
      globaldict["question3"]="1"
      textPrint("I can't help but feel slightly guilty")
      return choiceMaker(["1","Access granted","codeSite1"])
    else:
      globaldict["sattempt"]=globaldict["sattempt"]-1
      textPrint("Inorrect - " + str(globaldict["sattempt"]) + " attempts remain.")
      return choiceMaker(["1","Try again","question3","2","Cancel login attempt","serviceLogin"])
  
def codeSite1():
  globaldict["datab"]="1"
  if globaldict["deleted"]=="1":
    textPrint("It's all gone...")
    return choiceMaker(["1","Review choices","choice1"])
  else:
    textPrint("At last, something of value to Albert.\n\nThe site contains 3 programs Albert has been working on, I hope they're important to him.\n\nThere are 3 files")
    if globaldict["virus"]=="1":
      print("1rojec# 1\n-passwor# m*na5er\n-%tawr63&\n")
    else:
      print("project 1\npassword manager\nrtawr63w\n")
    return choiceMaker(["1","View the code","codeView","2","Add bugs to code","codeBugs","3","Remove comments from code","codeComments","4","Delete the code","codeDelete","5","Review choices","choice1"])

def codeView():
  if globaldict["virus"]=="1":
    textPrint("Nothing of importance, even the \"passwor$ m*na5er\" contains nothing of interest..&")
  else:
    textPrint("Nothing of importance, even the password manager contains nothing of interest..")
  return choiceMaker(["1","Go back","codeSite1"])

def codeComments():
  textPrint("If he forgets the purpose of a function or section of code, he's in trouble.")
  return choiceMaker(["1","Return to website homepage","codeSite1"])

def codeDelete():
  textPrint("Deleting his files is pretty exetreme, he's cleanly spent a lot of time working of these programs...")
  return choiceMaker(["1","Reconsider","codeSite1","2","Delete it","codeDelete2"])

def codeDelete2():
  textPrint("I never expected revenge to feel so sour...")
  globaldict["deleted"]="1"
  return choiceMaker(["1","Return to website homepage","codeSite1"])

def codeBugs():
  textPrint("Adding bugs should frustrate Albert without taking this too far")
  return choiceMaker(["1","Add logical errors","codeBugLogic","2","Add syntax errors","codeBugsSyntax"])

def codeBugLogic():
  textPrint("Logical errors will result in Albert having to debug his code without the assistance of any error messages.")
  return choiceMaker(["1","Return to website homepage","codeSite1"])

def codeBugsSyntax():
  textPrint("Syntax errors will cause frustration as he is constantly bombarded with error messages.")
  return choiceMaker(["1","Return to website homepage","codeSite1"])


def vpnAlbert():
  textPrint("What? A VPN can't just steal someones IP...")
  globaldict["vpnAlbert"]="1"
  return choiceMaker(["1","Go back","vpn1"]) 

def spamemail():
  textPrint("I spent at least an hour sharing Albert's emails to ensure they were riddled with spam, I hope they bypass the spam filters.")
  globaldict["spammed"]="1"
  return choiceMaker(["1","Go back","dataBreach"])

def dataleak():
  textPrint("What benefit would warning him serve me?")
  return choiceMaker(["1","Warn him anyway","Warnhim","2","Go back","dataBreach"])

def Warnhim():
  textPrint("I messaged him and showed him all the breached data relevant to him. Albert was surprised was the gesture, he didn't even question how I found the data. I told him of services such as \"https://haveibeenpwned.com/\" as to ensure he could protect himself in the future. Albert claimed that some of the data was still relevant and could've had disastrous results, he was surprisingly greatful. He apologized for his actions and as a result you became better friends.")
  globaldict["friendly"]="1"
  return choiceMaker(["1","Is that it?","ending"])


def ending():
  if globaldict["datab"]=="1":
    if globaldict["deleted"]=="1":
      textPrint("I took this too far, deleting his programs was unncessary...")
    else:
      textPrint("I messed with his programs and I'm certain he'll take notice; I could've done a lot worse.")
  
  if globaldict["reported"]=="1":
    textPrint("Reporting Albert's social media posts was meaningless, but at least it felt good.")

  if globaldict["spammed"]=="1":
    textPrint("I spammed all of Albert's emails by using a variety of websites, he'll either have to make a new email account or delete the spam himself")

  if globaldict["ddos"]=="1":
    textPrint("Maybe in another world I would've been able to DDOS Albert.")

  if globaldict["virus"]=="1":
    textPrint("I'5l s#an 3y PC fo/ virus3s t&mo$row.")

  if globaldict["datab"]=="0" and globaldict["reported"]=="0" and globaldict["spammed"]=="0" and globaldict["friendly"] =="1":
    textPrint("I'm glad I was able to remain friends with Albert. Petty revenge isn't worth it.")
  elif globaldict["friendly"] =="1":
    textPrint("Whilst me and Albert are friends again, I hope he isn't too vengeful when he discovers my revenge.")

  if globaldict["datab"]=="0" and globaldict["reported"]=="0" and globaldict["spammed"]=="0" and globaldict["friendly"] =="0":
    textPrint("I didn't get my revenge")
  time.sleep(1000)
  textPrint("The game has ended")
  time.sleep(1000**10)
  

# Used to run each function when 
while True:
  exec("runSection=%s()" % (runSection))
    
