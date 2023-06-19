import json
import streamlit as st
import requests


def run():
    option = st.selectbox(
        'Select the type of generative AI?',
        ('Text Prompt', 'Chat Prompt', 'Fine Tune Prompt'), )
    st.write('You selected:', option)

    if option == 'Text Prompt':
        input_text = st.text_input(label="Enter the input text")
        data = {
            "input_text": input_text,
            "input_type": option
        }
        if st.button("output"):
            resp = requests.post("http://172.16.200.30:10179/vertex", json=data)
            print(resp.text)
            json_data = json.loads(resp.text)
            st.json(json_data)

    elif option == 'Chat Prompt':
        input_text = st.text_input(label="Enter the input text")
        data = {
            "input_text": input_text,
            "input_type": option
        }
        if st.button("output"):
            resp = requests.post("http://172.16.200.30:10179/vertex", json=data)
            print(resp.text)
            json_data = json.loads(resp.text)
            st.json(json_data)


if __name__ == '__main__':
    run()
