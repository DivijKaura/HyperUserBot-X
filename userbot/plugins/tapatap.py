import asyncio

from ..utils import admin_cmd


@borg.on(admin_cmd(pattern="tapatap ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await event.edit("Nipple 😋 se Tapak Raha Hai Pasina😥")
        await asyncio.sleep(2)
        await event.edit("Nipple 🤭 se Tapak Rha h pasina🤤")
        await asyncio.sleep(2)
        await event.edit("Bhegi💦 hui gand, Aur lathpath Seena🤭")
        await asyncio.sleep(2)
        await event.edit("Abb Tumhi btao Bhai🙄")
        await asyncio.sleep(2)
        await event.edit("Itni garmi me😰 \n Koi Kaise Thoke Hasina😵")
        await asyncio.sleep(3.5)
        await event.edit(
            "Nipple Se Tapak Raha Hai Pasina💦 \nNipple Se Tapak Raha Hai Pasina💦 \nBhigi Hui Gaand🤭 Aur Lathpath Seena😐 \nAab Tumhi Batao bhai🙄 \nItni Garmi Mein😰 Koi Kaise Thoke😵 Hasina😋"
        )
