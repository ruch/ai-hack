import streamlit as st
import openai
# Set your OpenAI API key here

def generate_learning_material(topic, available_time):
    system_message = "You are a teacher who breaks down complex or difficult topics into simple and easy to understand learning material for 15-year-olds. Only focus on the most important points. Breakout the text in suitable paragraphs."
    user_message = f"Generate a brief learning material about {topic} that I can understand in {available_time} minutes."

    lconversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]

    conversation = f"{system_message}\n{user_message}\n"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=conversation,
        max_tokens=300,  # Adjust as needed
        temperature=0.4  # Adjust the temperature for response randomness
    )

    return response.choices[0].text.strip()

def main():
    st.title("Learning Platform on the go")
    #st.write("How much time you have?")
    #st.write("What do you want to learn?")

    available_time = st.slider("Select time you have to learn (minutes)", min_value=10, max_value=120, value=5, step=5)
    selected_topic = st.text_input("What do you want to learn?")

    if selected_topic:
        learning_material = generate_learning_material(selected_topic, available_time)
        st.subheader(f"Learning Material for '{selected_topic}' ({available_time} minutes):")
        st.write(learning_material)

st.button("What to continue learning?") 


if __name__ == "__main__":
    main()
