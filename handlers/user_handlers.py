from aiogram import F, Router
from aiogram.types import Message
import openai
from config import load_config

openai.api_key = load_config().openai_token
router: Router = Router()


async def chat(text: str) -> str:
    response = await openai.Completion.acreate(
        model="text-davinci-003",
        prompt=text,
        temperature=0.5,
        max_tokens=2000
    )
    return response["choices"][0]["text"]


@router.message(F.content_type == 'text')
async def process_message(message: Message):
    """Принимает все текстовые сообщения."""
    answer = await chat(message.text)
    await message.reply(text=answer)
