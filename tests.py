from pyrogram import Client
from pyrogram import Client, filters
bot_token="6787342834:AAFlt-K5BnJ0AEV2kJIooKY7L9UievGi8SY"
api_id = 26584939

api_hash = "04d310987225860f27c9196823e0251d"
app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)


@app.on_message(filters.text & filters.private)
async def echo(client, message):
    await message.reply(message.text)

app.run()