import streamlit as st
import openai
from textwrap3 import wrap
st.title("CAP4936: Special Topics in Data Analytics with Dr. Lee")
st.sidebar.header("Instructions")
st.sidebar.info(
    '''This is a web application that allows you to interact with 
       the OpenAI API's implementation of the ChatGPT model.
       Enter a **query** in the **text box** and **press enter** to receive 
       a **response** from the ChatGPT
       '''
    )
st.sidebar.image('https://clipground.com/images/miami-dade-college-logo-7.png', width=100)
model_engine = 'text-davinci-003'
openai.api_key = "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"
def main():
    '''
    This function gets the user input, pass it to ChatGPT function and 
    displays the response
    '''
    # Get user input
    user_query = st.text_input("Enter query here, to exit enter :q", "what is Python?")
    if user_query != ":q" or user_query != "":
        # Pass the query to the ChatGPT function
        response = ChatGPT(user_query)
        return st.write(f"{user_query} {response}")

def ChatGPT(user_query):
    ''' 
    This function uses the OpenAI API to generate a response to the given 
    user_query using the ChatGPT model
    '''
    # Use the OpenAI API to generate a response
    completion = openai.Completion.create(
                                  engine = model_engine,
                                  prompt = user_query,
                                  max_tokens = 1024,
                                  n = 1,
                                  temperature = 0.5,
                                      )
    # response = completion.choices[0].text
    response = completion.choices[0]["text"].replace("\n", "")
    formatted_response = wrap.indent(text=response, prefix='    ')
    return response
main()
