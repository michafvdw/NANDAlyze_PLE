import streamlit as st
import openai



st.write("## this is a H2 Title!")
st.write("hello world")

x = st.text_input("Image URL")
y = st.text_input("Role of the LLM")
z = st.text_input("Prompt")

st.write(f"Your image URL is: {x}")
st.write(f"The role is: {y}")
st.write(f"The prompt is: {z}")

is_clicked = st.button("Generate description")



# Set your Azure OpenAI API credentials and parameters
api_base = 'https://chatbotters.openai.azure.com/'  # Replace with your Azure OpenAI endpoint
api_key = "06bad53ccf0e44c88a03e939bea07600"  # Replace with your actual API key
deployment_name = 'GPT4Vision'
api_version = '2024-02-15-preview'  # Ensure this is the correct version

# Configure OpenAI API
openai.api_type = "azure"
openai.api_base = api_base  # This should be your Azure OpenAI API endpoint
openai.api_key = api_key
openai.api_version = api_version

if is_clicked and x and z and y:

        # Example usage of the Azure OpenAI API (chat completion)
        response = openai.ChatCompletion.create(
            engine=deployment_name,  # Azure's deployment name is passed as 'engine'
            #messages=[
                #{"role": "system", "content": "You are a helpful assistant that can access images online."},
                #{"role": "user", "content": f"Please describe the image at this URL: {x}"}
            messages=[
                { "role": "system", "content": f"{y}" },
                { "role": "user", "content": [  
                    { 
                        "type": "text", 
                        "text": f"{z}"
                    },
                    { 
                        "type": "image_url",
                        "image_url": {
                            "url": f"{x}"
                        }
                    }
                ] } 
            ],
            #],
            max_tokens=2000
        )
        
        # Extract and display the response content
        st.write(response['choices'][0]['message']['content'])
