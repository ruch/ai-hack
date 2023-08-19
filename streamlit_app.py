import streamlit as st
import openai
#import os



# Set your OpenAI API key here
#openai.api_key = os.environ['OPENAI_API_KEY']

def generate_learning_material(topic, available_time):
    prompt = f"Explain {topic} that a 15-year-old can understand in {available_time} minutes. Only focus on the most important points. Breakout the text in suitable paragraphs."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=300,  # Adjust as needed
        stop=None,
        temperature=0.2  # Adjust the temperature for response randomness
    )

    return response.choices[0].text.strip()

def main():
    st.title("Quick Learning Platform for 15-year-olds")
    st.write("Input the time you have and the topic you want to learn about.")

    available_time = st.slider("Select available time (minutes)", min_value=10, max_value=120, value=30, step=10)
    selected_topic = st.text_input("Enter a topic")

    if selected_topic:
        learning_material = generate_learning_material(selected_topic, available_time)
        st.subheader(f"Learning Material for '{selected_topic}' ({available_time} minutes):")
        st.write(learning_material)

if __name__ == "__main__":
    main()
