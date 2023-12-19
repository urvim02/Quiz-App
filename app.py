import streamlit as st
import langchain
import openai
from backend_logic import generate_question, generate_answer_options,generate_quiz

openai.api_key = "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"

st.title("Quiz Generator")

topic = st.text_input("Enter your preferred quiz topic")
number_of_questions = st.slider("Number of questions", 1, 10, 5)
if st.button("Generate Quiz"):
    quiz_data = generate_quiz(topic, number_of_questions)

    for index, (question, options, correct_answer) in enumerate(quiz_data):
        user_answer = st.multiselect(f"{index + 1}. {question}", options, options)
        if st.button("Submit"):
            if correct_answer in user_answer:
                st.write("Correct!")
            else:
                st.write("Incorrect. The correct answer is:", correct_answer)