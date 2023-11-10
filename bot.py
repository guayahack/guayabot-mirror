from discord import Intents, Client
import responses, logging

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        
        # Check if response is not empty
        if response:
            if is_private:
                await message.author.send(response)
            else:
                await message.channel.send(response)
    except Exception:
        logging.exception("Exception in bot(): ")

def run_discord_bot():
    with open("token.txt", "r") as f: # Lee el token del archivo token.txt y lo guarda en la variable TOKEN
        TOKEN = f.read()
    
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)

    @client.event
    async def on_ready():
        logging.info("{client_user} is now running!")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = message.content.strip()  # Elimina espacios en blanco alrededor del mensaje

        # Verifica si el mensaje no está vacío
        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)  # Mueve esta línea aquí

# Llama a la función para ejecutar el bot
run_discord_bot()
