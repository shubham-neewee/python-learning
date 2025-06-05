# Install an External module and perform an operation of your own interst

# This will import the library
import pyttsx3

#The below will initialise the python pyttxs engine -  # object creation
engine = pyttsx3.init()


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 150)     # setting up new voice rate


# The below text will be the text that the engine will read
engine.say('''
In 1964, the expression READ-EVAL-PRINT cycle is used by L. Peter Deutsch and Edmund Berkeley for an implementation of Lisp on the PDP-1.[3] Just one month later, Project Mac published a report by Joseph Weizenbaum (the creator of ELIZA, the world's first chatbot) describing a REPL-based language, called OPL-1, implemented in his Fortran-SLIP language on the Compatible Time Sharing System (CTSS).[4][5][6]

The 1974 Maclisp reference manual by David A. Moon attests "Read-eval-print loop" on page 89, but does not use the acronym REPL.[7]

Since at least the 1980s, the abbreviations REP Loop and REPL are attested in the context of Scheme.[8][9]
           ''')

# Once the execution is done then the engine will stop
engine.runAndWait()