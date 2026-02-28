from openai import OpenAI 
import streamlit as st
import os 

# give the title of the project
st.title("ChatStream")

# initialize the Ollama client 
if 'model' not in st.session_state:
    # Ollama runs locally on port 11434 by default
    st.session_state['model'] = OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama', 
    )
     
# initialize session variable
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    
# create a sidebar to adjust parameters
st.sidebar.title('Model Parameters')


selected_model = st.sidebar.selectbox("Select Model", ["llama3:latest", "gemma3:1b"])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
max_tokens= st.sidebar.slider("Max Tokens", min_value=1, max_value=4096, value=512)

# update the interface with previous messages
for message in st.session_state['messages']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
# create chat interface
if prompt := st.chat_input("Enter your query."):
    st.session_state['messages'].append({'role':'user', 'content':prompt}) 
    with st.chat_message('user'):
        st.markdown(prompt)
        
    # get response from model
    with st.chat_message('assistant'):
        client = st.session_state['model']
        try:
            stream = client.chat.completions.create(
                model=selected_model,
                messages=[
                    {'role': m['role'], 'content': m['content']}
                    for m in st.session_state['messages']
                ],
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True
            )
            response = st.write_stream(stream)

        except Exception as e:
            response = "Error generating response."
            st.error(str(e))
    st.session_state['messages'].append({'role': 'assistant', 'content': response})