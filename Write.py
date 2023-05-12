#also do: pip install streamlit
import streamlit as st

#to connect Python with ChatGPT, use: import openai
#in the command line, type: pip install openai
import openai

#get an API key at https://platform.openai.com/account/api-keys
#better to use OS environmental variables (?)
openai.api_key = "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"

#this is the function for sending a prompt to ChatGPT
def BasicGeneration(userPrompt):
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=userPrompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completion.choices[0].text
    return message.strip()

#title
st.title("I will write you a children's story about a virtue!")

# define the possible virtues
virtues = [
    "kindness (thoughtful, considerate)", 
    "trustworthiness (honesty, reliability)", 
    "friendliness (including others, thoughtfulness)", 
    "contentment (gratitude, thankfulness, not complaining)", 
    "courtesy (good manners, politeness)",
    "justice (fairness, equality, helping someone who has been wronged)", 
    "gentleness (not rough or rude)", 
    "confidence (developing and using your skills)", 
    "courage (doing what is good or right even when you are scared)", 
    "responsibility (doing a good job, starting and ending work on time, taking care of things)",
    "gratitude (saying thank you, showing appreciation)", 
    "respect (not interrupting or arguing, treating everyone properly)", 
    "perseverance (resiliency, problem solving, finishing something hard)", 
    "patience (waiting cheerfully, not losing your temper)", 
    "generosity (sharing your time, money or things)",
    "wisdom (maturity, making good choices)", 
    "creativity (thinking of unusual activities or solutions)", 
    "good humor (cheerfulness, making jokes that don't hurt feelings)", 
    "compassion (empathy, sympathy)", 
    "humility (being a good sport, not boasting, pointing out the good in others)", 
    "diplomacy (the best way to say something to build good feelings in others)",
    "self-control (self-discipline, restraint)", 
    "optimism (hopefulness, positive outlook)", 
    "forgiveness (restoring relationships, not becoming bitter or resentful)", 
    "cooperativeness (working well with others)", 
    "doing what is right (uprightness, obedience)"
]

# ask user to select a virtue from the dropdown list
selected_virtue = st.selectbox("Select a virtue to base the story on:", virtues)

# choose a reading level at which the story should be written
gradelevels = ["2nd", "5th", "8th",  "11th"]

reading_level = st.selectbox("At what grade level (reading level) should the story be written?", gradelevels)

# create dictionary mapping reading levels to grade levels
reading_to_grade = {"2nd": 2, "5th": 5, "8th": 8, "11th": 11}

# look up grade level based on reading level
gradeyear = reading_to_grade.get(reading_level)
booklength = 20 + (gradeyear * 3)
character_age = gradeyear + 5 

# ask for the main character's name and age
character_name = st.text_input("What is the main character's name?")
character_age = st.slider("How old is the main character?", 5, 15)

#ask for the main character's gender
genders = ["female", "male", "unspecified"]
selected_gender = st.selectbox("Choose a gender for the main character:", genders)
pronouns = "they/them"
if selected_gender == "female": 
    pronouns = "she/her"
if selected_gender == "male":    
    pronouns = "he/him"

# generate the prompt based on the selected virtue
prompt = f"You are the author of children's short stories with 20 years of experience, and you are especially good at writing virtue tales and bedtime stories with a good sense of humor, interesting details, and good dialogue.  For this short story, the theme is the virtue of {selected_virtue} and the story arc is that the main character lacks this virtue at the beginning of the story and develops it by the end.  The character is named {character_name} and their pronouns are {pronouns} and is {character_age} years old, so choose scenarios appropriate to the character's age.  The characters should have interesting names.  Begin with a scene in which the character fails to use the virtue of {selected_virtue} and there is a negative outcome to the main character or someone else.  Be sure to include some dialogue to illustrate how the main character recognizes the problem, maybe through a discussion with a friend or mentor.  Near the end of the short story, include another scene in which the main character has another opportunity to use or display the virtue of {selected_virtue} and what the positive outcome is. You should also make the story appropriate for a reader at the {gradelevels} grade level, using words that the reader will know and a story length they will be able to read in about five minutes.  Please use a low temperature setting to ensure that the story is structured and coherent.  The story must be completely appropriate for young children and absolutely cannot include death, violence, blood, crime, suicide, abuse, rape, weapons, sex, dating, bad language, bullies, bullying, hitting, or anything else that would be inappropriate for children.  When writing out the story, begin with an interesting title; then separate the rest of the story into groups of 1-5 sentences (or paragraphs) that will be on the same page when the book is printed."

button_placeholder = st.empty()
if button_placeholder.button('Start Writing'):
    #hide the button
    button_placeholder.empty()
    with st.spinner('Generating a story from the AI...'):
        #get the story
        response = BasicGeneration(prompt) 
        st.write(response)
        st.success('Done!  To write another story, make your selections again.  Sometimes the AI comes up with a good story but sometimes it takes a few tries....')
     
  