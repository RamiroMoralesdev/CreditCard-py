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
    credit_card_entidad_image: rx.Component = None

    if credit_card_number == '':
        credit_card_number = '000 000 000 000'
        credit_card_name = 'John Doe'
        credit_card_created = '00/00'
        credit_card_date = '00/00'
        credit_card_cvv = '000'
        credit_card_entidad = 'MasterCard'
        credit_card_entidad_image = 'mastercard.png'
    else:
        credit_card_number = credit_card_number 
        credit_card_name = credit_card_name
        credit_card_date = credit_card_date
        credit_card_cvv = credit_card_cvv
        credit_card_entidad = credit_card_entidad

    if credit_card_entidad == 'MasterCard':
        credit_card_entidad = credit_card_entidad

    
    def update_credit_card_number(self, number: str):
        self.credit_card_number = number

    def update_credit_card_name(self, name: str):
        self.credit_card_name = str(name)

    def update_credit_card_created(self, created: str):
        self.credit_card_created = created

    def update_credit_card_date(self, date: str):
        self.credit_card_date = date

    def update_credit_card_cvv(self, cvv: str):
        self.credit_card_cvv = cvv

    def update_credit_card_entidad(self, entidad: str):
        self.credit_card_entidad = entidad
        if entidad == 'MasterCard':
            self.credit_card_entidad_image = "mastercard.png"
        elif entidad == 'Visa':
            self.credit_card_entidad_image = "visa.png"
        elif entidad == 'American Express':
            self.credit_card_entidad_image = "american_express.png"
        else:
            self.credit_card_entidad_image = None


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        # Input Credit Card Number
        rx.box(
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
            placeholder="Enter Credit Card Created",
            width="100%",
            height="50px",
            border="1px solid #000",
            border_radius="5px",
            on_change=State.update_credit_card_created,
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
        )
        ), 
        
        # Credit Card Information
        rx.box(
            rx.box(
                rx.text("Python SA.", font_size="24px", color="black"),
            ),
            rx.box(
                rx.text(State.credit_card_number, font_size="40px", font_weight="bold", id="credit_card_number", color="white"),

                margin_top="50px",
                margin_bottom="0",
            ),
            rx.box(
                rx.text( "Created: " + State.credit_card_created, font_size="24px", font_weight="bold", id="credit_card_created", color="white"),
                rx.text( "Expired: " + State.credit_card_date, font_size="24px", font_weight="bold", id="credit_card_date", color="white"),

                margin_top="15%",
                display="flex",
                flex_direction="row",
                gap="20px",
            ),

            rx.box(
                rx.text(State.credit_card_name, font_size="24px", font_weight="bold", id="credit_card_name", color="white"),
            ),
            
            rx.box(
                rx.text(State.credit_card_cvv, font_size="24px", font_weight="bold", id="credit_card_cvv", color="white"),
                rx.text(State.credit_card_entidad, font_size="24px", font_weight="bold", id="credit_card_entidad", color="white"),
                rx.image(src=State.credit_card_entidad_image, width="100px", height="100px", margin_left="120px" ),

                display="flex",
                flex_direction="row",
                gap="20px",
            ),
            

            width="500px",
            height="350px",
            bg="linear-gradient(45deg, #ffb465, #af7c4b)",
            margin="0 auto",
            border_radius="15px",
            padding="20px",
            display="flex",
            flex_direction="column",
        ),

        # Styles of element father
        width="100%",
        height="100%",
        padding="20px",
        display="flex",
        flex_direction="row",
        align_items="center",
        justify_content="center",
    ),


def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading(
            "PRODUCTS", size="4", weight="bold", as_="h3"
        ),
        footer_item("Web Design", "/#"),
        footer_item("Web Development", "/#"),
        footer_item("E-commerce", "/#"),
        footer_item("Content Management", "/#"),
        footer_item("Mobile Apps", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

app = rx.App()
app.add_page(index)
