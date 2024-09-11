"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    credit_card_number: str = ''
    credit_card_name: str = ''
    credit_card_date: str = ''
    credit_card_cvv: str = ''
    credit_card_entidad: str = ''
    if credit_card_number == '':
        credit_card_number = '000 000 000 000'
        credit_card_name = 'John Doe'
        credit_card_date = '00/00'
        credit_card_cvv = '000'
        credit_card_entidad = 'MasterCard'
    else:
        credit_card_number = credit_card_number 
        credit_card_name = credit_card_name
        credit_card_date = credit_card_date
        credit_card_cvv = credit_card_cvv
        credit_card_entidad = credit_card_entidad

    def update_credit_card_number(self, number: str):
        self.credit_card_number = number

    def update_credit_card_name(self, name: str):
        self.credit_card_name = str(name)

    def update_credit_card_date(self, date: str):
        self.credit_card_date = date

    def update_credit_card_cvv(self, cvv: str):
        self.credit_card_cvv = cvv

    def update_credit_card_entidad(self, entidad: str):
        self.credit_card_entidad = entidad


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        # Input Credit Card Number
        rx.input(
            placeholder="Enter Credit Card Number",
            width="100%",
            height="50px",
            border="1px solid #000",
            border_radius="5px",
            on_change=State.update_credit_card_number,
        ),

        rx.input(
            placeholder="Enter Credit Card Name",
            width="100%",
            height="50px",
            border="1px solid #000",
            border_radius="5px",
            on_change=State.update_credit_card_name,
        ),

        rx.input(
            placeholder="Enter Credit Card Date",
            width="100%",
            height="50px",
            border="1px solid #000",
            border_radius="5px",
            on_change=State.update_credit_card_date,
        ),

        rx.input(
            placeholder="Enter Credit Card CVV",
            width="100%",
            height="50px",
            border="1px solid #000",
            border_radius="5px",
            on_change=State.update_credit_card_cvv,
        ),

        rx.select(
            [
                "MasterCard",
                "Visa",
                "American Express",
            ],
            on_change=State.update_credit_card_entidad,
            placeholder="Select Credit Card Entidad",
            width="100%",
            border="1px solid #000",
            border_radius="5px",
        ),
        
        # Credit Card Information
        rx.box ( style = {
            "background-color": "red",
        },
            
        rx.box(
            rx.text("Python SA.", font_size="24px", ),
        ),
        rx.box(
            rx.text(State.credit_card_number, font_size="24px", font_weight="bold", id="credit_card_number"),

            rx.text(State.credit_card_name, font_size="24px", font_weight="bold", id="credit_card_name"),
        ),

        rx.box(
            rx.text(State.credit_card_date, font_size="24px", font_weight="bold", id="credit_card_date"),
        ),

        rx.box(
            rx.text(State.credit_card_cvv, font_size="24px", font_weight="bold", id="credit_card_cvv"),
        ),

        rx.box(
            rx.text(State.credit_card_entidad, font_size="24px", font_weight="bold", id="credit_card_entidad"),
        )

        )
    )



    style = {
        "Container-Information": {
            "background-color": "red",
            "color": "#fff",
            "padding": "20px",
            "border_radius": "10px",
        }
    }
    

app = rx.App()
app.add_page(index)
