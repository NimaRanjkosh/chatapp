"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from chatapp import style

class State(rx.State):
    """The app state."""

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                question,
                style=style.question_style,
            ),
            text_align="right"
        ),
        rx.box(
            rx.text(
                answer,
                style=style.answer_style,
            ),
            text_align="left"  
        ),
        margin_y="1em",
        width="100%"
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "Reflex is a Python web framework for building real-time web applications."
        ),
        (
            "How do I install Reflex?",
            "You can install Reflex using pip: pip install reflex."
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
          placeholder="Ask anything",
          style=style.input_style,
        ),
        rx.button("Ask", 
                  style=style.button_style,
                  on_click=print("did clicked")),
    )

def index() -> rx.Component:
    
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
    )


app = rx.App()
app.add_page(index)
