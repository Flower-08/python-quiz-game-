import random
import streamlit as st

# Your quiz questions
quiz_dict = [
    {
        "number": "1",
        "question": "Number of continents in the world?",
        "answer": "Seven"
    },
    {
        "number": "2",
        "question": "What is the capital city of France?",
        "answer": "Paris"
    },
    {
        "number": "3",
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "number": "4",
        "question": "What is the largest ocean on Earth?",
        "answer": "Pacific Ocean"
    },
    {
        "number": "5",
        "question": "Which is the longest river in South America?",
        "answer": "Amazon"
    },
    {
        "number": "6",
        "question": "Which country has the largest population in the world?",
        "answer": "India"
    },
    {
        "number": "7",
        "question": "What is the largest mammal in the world?",
        "answer": "Blue Whale"
    },
    {
        "number": "8",
        "question": "Which language has the most native speakers worldwide?",
        "answer": "Mandarin Chinese"
    },
    {
        "number": "9",
        "question": "What is the capital city of Australia?",
        "answer": "Canberra"
    },
    {
        "number": "10",
        "question": "Which country has the most time zones, including overseas territories?",
        "answer": "France"
    }
]


# Start a new game
def start_game():
    st.session_state.questions = random.sample(quiz_dict, 5)
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.game_finished = False


# Start the game the first time
if "questions" not in st.session_state:
    start_game()


# Title
st.title("🎯 Python Quiz Game")

# Game finished
if st.session_state.game_finished:

    st.header("🎉 Quiz Complete!")

    st.write(
        f"You scored **{st.session_state.score} out of 5**!"
    )

    if st.session_state.score == 5:
        st.success("🏆 Perfect score!")
    elif st.session_state.score >= 3:
        st.success("👏 Well done!")
    else:
        st.info("Keep practising and try again!")

    if st.button("🔄 Play Again"):
        start_game()
        st.rerun()


# Quiz in progress
else:

    current = st.session_state.current_question
    question = st.session_state.questions[current]

    st.write(f"### Question {current + 1} of 5")

    st.write(f"**{question['question']}**")

    # Answer box
    answer = st.text_input(
        "Your answer:",
        key=f"answer_{current}",
        disabled=st.session_state.answered
    )

    # Submit answer
    if not st.session_state.answered:

        if st.button("Submit Answer"):

            if answer.strip().lower() == question["answer"].lower():

                st.success("✅ Correct! You gained a point.")
                st.session_state.score += 1

            else:

                st.error("❌ Incorrect! Your points remain the same.")

                st.info(
                    f"The correct answer was: **{question['answer']}**"
                )

            st.session_state.answered = True
            st.rerun()


    # Next question button
    else:

        if current < 4:

            if st.button("➡️ Next Question"):

                st.session_state.current_question += 1
                st.session_state.answered = False
                st.rerun()

        else:

            if st.button("🏁 See Final Score"):

                st.session_state.game_finished = True
                st.rerun()