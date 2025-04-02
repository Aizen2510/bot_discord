import discord
from google import genai
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

genai_client = genai.Client(api_key="api-genmini")

troll_user_id = # id you want
name = "Chó Ngu"
target_user_id = # id you want
nickname = "Bố"


async def process_message(message):
    if message.author.bot:
        return
    
    if message.author.id == troll_user_id:
        greeting = f"Bố Chào {name}, "
    elif message.author.id == target_user_id:
        greeting = f"Con Chào {nickname},"
    else:
        greeting = "Tao "

    user_input = message.content

    if "tiếng Anh" in user_input or "English" in user_input:
        response_text = "Tao Nói Tiếng Việt chứ không nói tiếng Anh."
    else:
        user_input_vn = f"Đéo Biết: {user_input}"
        response = genai_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[user_input_vn]
        )
        response_text = response.text

    await message.channel.send(greeting + response_text)


@client.event
async def on_ready():
    print(f'Bot đã đăng nhập dưới tên {client.user}')


@client.event
async def on_message(message):
    await process_message(message)

client.run('your-token') 
