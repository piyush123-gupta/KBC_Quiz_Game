from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

# Initialize the text-to-speech engine
engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize the mixer for playing audio
mixer.init()

mixer.music.load('KBC/kbc.mp3')     # Load the background music
mixer.music.play(-1)                # Play the music in a loop

# Function to handle the selection of an answer
def select(event):
    # Hide all progress bars and labels
    callButton.place_forget()
    ProgressbarA.place_forget()
    ProgressbarB.place_forget()
    ProgressbarC.place_forget()
    ProgressbarD.place_forget()
    
    ProgressbarLabelA.place_forget()
    ProgressbarLabelB.place_forget()
    ProgressbarLabelC.place_forget()
    ProgressbarLabelD.place_forget()
    
    # Get the selected answer 
    b=event.widget
    value=b['text']
    
    # Check if the selected answer is correct
    for i in range(15):
        if value==correct_answers[i]:
            # If the last question is answered correctly, show the win screen
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()
                    
                def playagain():
                    # Reset the game state
                    lifeline50Button.config(state=NORMAL,image=image50)
                    audiencePoleButton.config(state=NORMAL,image=audiencePole)
                    phoneLifeLineButton.config(state=NORMAL,image=phoneImage)
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END,questions[0])
                            
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                            
                    amountLabel.config(image=amountimage)
                
                # Stop the background music and play the win music
                mixer.music.stop()
                mixer.music.load('KBC/Kbcwon.mp3')
                mixer.music.play()
                
                
                # Create a new window for the win screen                
                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title("You won 0 pounds")
                imgLabel=Label(root2,image=centerImage,bd=0)
                imgLabel.pack(pady=30)
                                
                winLabel= Label(root2, text="You Won",font=('arial',40,'bold'),bg='black',fg='white')
                winLabel.pack()
                                
                                
                playagainButton=Button(root2,text='Play Again',font=('arial', 20, 'bold'),bg='black',fg='white',
                                                    activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=playagain)
                playagainButton.pack()
                                
                closeButton=Button(root2,text='Close',font=('arial', 20, 'bold'),bg='black',fg='white',
                                                    activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=close)
                closeButton.pack()
                                
                happyimage=PhotoImage(file='KBC/happy.png')
                happyLabel=Label(root2,image=happyimage,bg='black',bd=0)
                happyLabel.place(x=30,y=280)
                                
                happyLabel1=Label(root2,image=happyimage,bg='black',bd=0)
                happyLabel1.place(x=400,y=280)
                
                root2.mainloop()
                break
                
            
            # Update the question and options for the next question
            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])
            
            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            
            amountLabel.config(image=amountimages[i])
        
        # If the selected answer is incorrect, show the lose screen
        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()
            
            def tryagain():
                # Reset the game state
                lifeline50Button.config(state=NORMAL,image=image50)
                audiencePoleButton.config(state=NORMAL,image=audiencePole)
                phoneLifeLineButton.config(state=NORMAL,image=phoneImage)
                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END,questions[0])
                
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                
                amountLabel.config(image=amountimage)
            
            # Create a new window for the lose screen
            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title("You won 0 pounds")
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)
            
            loseLabel= Label(root1, text="You Lose",font=('arial',40,'bold'),bg='black',fg='white')
            loseLabel.pack()
            
            tryagainButton=Button(root1,text='Try Again',font=('arial', 20, 'bold'),bg='black',fg='white',
                                activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=tryagain)
            tryagainButton.pack()
            
            closeButton=Button(root1,text='Close',font=('arial', 20, 'bold'),bg='black',fg='white',
                                activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=close)
            closeButton.pack()
            
            sadimage=PhotoImage(file='KBC/sad.png')
            sadLabel=Label(root1,image=sadimage,bg='black',bd=0)
            sadLabel.place(x=30,y=280)
            
            sadLabel1=Label(root1,image=sadimage,bg='black',bd=0)
            sadLabel1.place(x=400,y=280)
            
            root1.mainloop()
            break
            
# Function to handle the 50-50 lifeline
def lifeline50():
    lifeline50Button.config(image=image50X,state=DISABLED)
    # Remove two incorrect options based on the current question
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')
    
    # ... (similar logic for other questions)
    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton2.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton1.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton2.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton2.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton2.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton1.config(text='')
        optionButton3.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text='')
        optionButton4.config(text='')
        
    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')
        
        
# Function to handle the audience poll lifeline
def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePoleX,state=DISABLED)
    # Show the progress bars and labels for the audience poll
    ProgressbarA.place(x=580,y=190)
    ProgressbarB.place(x=620,y=190)
    ProgressbarC.place(x=660,y=190)
    ProgressbarD.place(x=700,y=190)
    
    ProgressbarLabelA.place(x=580,y=320)
    ProgressbarLabelB.place(x=620,y=320)
    ProgressbarLabelC.place(x=660,y=320)
    ProgressbarLabelD.place(x=700,y=320)
    
    # Set the progress bar values based on the current question
    if questionArea.get(1.0,'end-1c')==questions[0]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=90)
        
    # ... (similar logic for other questions)
    if questionArea.get(1.0,'end-1c')==questions[1]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=30)
        
    if questionArea.get(1.0,'end-1c')==questions[2]:
        ProgressbarA.config(value=60)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=90)
        ProgressbarD.config(value=30)
        
    if questionArea.get(1.0,'end-1c')==questions[3]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=50)
        
    if questionArea.get(1.0,'end-1c')==questions[4]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=20)
        
    if questionArea.get(1.0,'end-1c')==questions[5]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=70)
        
    if questionArea.get(1.0,'end-1c')==questions[6]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=30)
        
    if questionArea.get(1.0,'end-1c')==questions[7]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=90)
        
    if questionArea.get(1.0,'end-1c')==questions[8]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=10)
        
    if questionArea.get(1.0,'end-1c')==questions[9]:
        ProgressbarA.config(value=90)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=30)
        
    if questionArea.get(1.0,'end-1c')==questions[10]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=90)
        
    if questionArea.get(1.0,'end-1c')==questions[11]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=90)
        ProgressbarD.config(value=40)
        
    if questionArea.get(1.0,'end-1c')==questions[12]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=50)
        
    if questionArea.get(1.0,'end-1c')==questions[13]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=50)
        ProgressbarC.config(value=90)
        ProgressbarD.config(value=20)
        
    if questionArea.get(1.0,'end-1c')==questions[14]:
        ProgressbarA.config(value=30)
        ProgressbarB.config(value=90)
        ProgressbarC.config(value=60)
        ProgressbarD.config(value=50)
        

# Function to handle the phone a friend lifeline
def phoneLifeLine():
    mixer.music.load('KBC/calling.mp3')
    mixer.music.play()
    callButton.place(x=70,y=260)
    phoneLifeLineButton.config(image=phoneImageX,state=DISABLED)

# Function to handle the phone call click
def phoneClick():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            engine.say(f'The answer is {correct_answers[i]}')
            engine.runAndWait()
        
# List of correct answers
correct_answers = ["Ganesha","Money","Jaipur","Paris","6","14 September","Brazil","New Delhi",
                "Nile","Vrindachal","Bangalore","Russia","Mars","Antarctic","Andes"]

# List of questions
questions = ["1: Which god is also known as 'Gauri Nandan'?",
            "2: What does not grow on tree according to a popular Hindi saying?",
            "3: Which city is known as the Pink City of India?",
            "4: The Eiffel Tower is located in which city?",
            "5: How many major religions are there in India?",
            "6: When is the National Hindi Diwas celebrated?",
            "7: Which country is the largest producer of coffee in the world?",
            "8: Where is India Gate located?",
            "9: What is the name of the longest river in the world?",
            "10: Which of the following is not a state of India?",
            "11: Which city is known as the 'Silicon Valley Of India'?",
            "12: Which country is the largest by land area?",
            "13: Which planet is known as the 'Red Planet'?",
            "14: What is the largest desert in the world?",
            "15: Which mountain range is the longest on Earth?"
            ]

# Lists of options for each question
first_option = ["Agni",
                "Money",
                "Banglore",
                "London",
                "6",
                "13 September",
                "Brazil",
                "Agra",
                "Amazon",
                "Vrindachal",
                "Delhi",
                "India",
                "Venus",
                "Sahara",
                "Himalayas"]

second_option = ["Indra",
                "Flowers",
                "Maysore",
                "Paris",
                "7",
                "14 September",
                "Colombia",
                "Punjab",
                "Nile",
                "Goa",
                "Mumbai",
                "China",
                "Mars",
                "Gobi",
                "Andes"]

third_option = ["Hanuman",
                "Leaves",
                "Jaipur",
                "Rome",
                "8",
                "14 July",
                "Vietnam",
                "Mumbai",
                "Yangtze",
                "Jharkhand",
                "Chennai",
                "Russia",
                "Jupiter",
                "Antarctic",
                "Alps"]

fourth_option = ["Ganesha",
                "Fruits",
                "Kochi",
                "Berlin",
                "9",
                "15 August",
                "Ethiopia",
                "New Delhi",
                "Mississippi",
                "Chattisgarh",
                "Bangalore",
                "United States",
                "Saturn",
                "Arabian",
                "Rocky"]

# Initialize the main application window
root=Tk()

root.geometry('1500x750+0+0')
root.title('Who wants to be a millionaire created by Dishank Singh')
root.config(bg='black')

# Create frames for organizing the layout
leftframe=Frame(root, bg='black',padx=90)
leftframe.grid(row=0, column=0)

topframe=Frame(leftframe,bg='black',padx=15)
topframe.grid(row=0, column=0 )

centerframe=Frame(leftframe,bg='black',padx=15)
centerframe.grid(row=1,column=0)

bottomframe=Frame(leftframe,bg='black')
bottomframe.grid(row=2,column=0)

rightframe=Frame(root,bg='black',pady=25,padx=50,background='black')
rightframe.grid(row=0, column=1)


# Load images for lifelines and buttons 
# Create buttons for lifelines
image50=PhotoImage(file='KBC/50-50.png')
image50X=PhotoImage(file='KBC/50-50-X.png')

lifeline50Button=Button(topframe,image=image50,bg='black',bd=0,activebackground='black',width=180,height=80,
                        command=lifeline50)
lifeline50Button.grid(row=0,column=0)

audiencePole=PhotoImage(file='KBC/audiencePole.png')
audiencePoleX=PhotoImage(file='KBC/audiencePoleX.png')

audiencePoleButton=Button(topframe,image=audiencePole,bg='black',bd=0,activebackground='black',width=180,height=80,
                        command=audiencePoleLifeline)
audiencePoleButton.grid(row=0,column=1)

phoneImage=PhotoImage(file='KBC/phoneAFriend.png')
phoneImageX=PhotoImage(file='KBC/phoneAFriendX.png')

phoneLifeLineButton=Button(topframe,image=phoneImage,bg='black',bd=0,activebackground='black',width=180,height=80
                        ,command=phoneLifeLine)
phoneLifeLineButton.grid(row=0,column=2)

callimage=PhotoImage(file='KBC/phone.png')

callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='black',cursor='hand2',
                command=phoneClick)

centerImage=PhotoImage(file='KBC/center.png')

# Create labels and buttons for the question and options
logoLabel=Label(centerframe,image=centerImage,bg='black',width=300,height=200)
logoLabel.grid(row=0, column=0)


amountimage=PhotoImage(file='KBC/Picture0.png')

amountimage1=PhotoImage(file='KBC/Picture1.png')
amountimage2=PhotoImage(file='KBC/Picture2.png')
amountimage3=PhotoImage(file='KBC/Picture3.png')
amountimage4=PhotoImage(file='KBC/Picture4.png')
amountimage5=PhotoImage(file='KBC/Picture5.png')
amountimage6=PhotoImage(file='KBC/Picture6.png')
amountimage7=PhotoImage(file='KBC/Picture7.png')
amountimage8=PhotoImage(file='KBC/Picture8.png')
amountimage9=PhotoImage(file='KBC/Picture9.png')
amountimage10=PhotoImage(file='KBC/Picture10.png')
amountimage11=PhotoImage(file='KBC/Picture11.png')
amountimage12=PhotoImage(file='KBC/Picture12.png')
amountimage13=PhotoImage(file='KBC/Picture13.png')
amountimage14=PhotoImage(file='KBC/Picture14.png')
amountimage15=PhotoImage(file='KBC/Picture15.png')

amountimages=[amountimage1, amountimage2, amountimage3, amountimage4, amountimage5, amountimage6, amountimage7,
            amountimage8, amountimage9, amountimage10, amountimage11, amountimage12, amountimage13, amountimage14, amountimage15]

amountLabel=Label(rightframe,image=amountimage,bg='black')   
amountLabel.grid(row=0, column=0)


layoutimage=PhotoImage(file='KBC/lay.png')

layoutimageLabel=Label(bottomframe,image=layoutimage,bg='black')   
layoutimageLabel.grid(row=0, column=0)

questionArea=Text(bottomframe,font=('areal',18,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70, y=10)

questionArea.insert(END, questions[0])


labelA=Label(bottomframe,text='A:',bg='black',fg='white',font=('arial',16,'bold'))
labelA.place(x=60,y=110)
optionButton1=Button(bottomframe,text=first_option[0],bg='black',fg='white',font=('arial',16,'bold'),bd=0,activebackground='black',
                    activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=105)


labelB=Label(bottomframe,text='B:',bg='black',fg='white',font=('arial',16,'bold'))
labelB.place(x=330,y=110)
optionButton2=Button(bottomframe,text=second_option[0],bg='black',fg='white',font=('arial',16,'bold'),bd=0,activebackground='black',
                    activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=105)

labelC=Label(bottomframe,text='C:',bg='black',fg='white',font=('arial',16,'bold'))
labelC.place(x=60,y=190)
optionButton3=Button(bottomframe,text=third_option[0],bg='black',fg='white',font=('arial',16,'bold'),bd=0,activebackground='black',
                    activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=185)

labelD=Label(bottomframe,text='D:',bg='black',fg='white',font=('arial',16,'bold'))
labelD.place(x=330,y=190)
optionButton4=Button(bottomframe,text=fourth_option[0],bg='black',fg='white',font=('arial',16,'bold'),bd=0,activebackground='black',
                    activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=185)

# Create progress bars for the audience poll
ProgressbarA=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarB=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarC=Progressbar(root,orient=VERTICAL,length=120)
ProgressbarD=Progressbar(root,orient=VERTICAL,length=120)

ProgressbarLabelA=Label(root,text='A', font=('arial',15,'bold'),bg='black',fg='white')
ProgressbarLabelB=Label(root,text='B', font=('arial',15,'bold'),bg='black',fg='white')
ProgressbarLabelC=Label(root,text='C', font=('arial',15,'bold'),bg='black',fg='white')
ProgressbarLabelD=Label(root,text='D', font=('arial',15,'bold'),bg='black',fg='white')

# Bind the select function to the option buttons
optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)

# Start the main event loop
root.mainloop()