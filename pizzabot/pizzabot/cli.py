from pizzabot.input import InputType, create_input
from pizzabot.bot import Bot

def run() -> None:
    """Method used to run the pizzabot using CLI"""
    cli_input = create_input(InputType.SysArgvInput)
    bot = Bot(cli_input)
    text_instructions = bot.get_text_instructions()
    print(text_instructions)