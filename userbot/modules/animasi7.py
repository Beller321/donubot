#greyyvbss 

import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, cilik_cmd 
  
  
@cilik_cmd(pattern="emon(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Cilik-Userbot....")
    animation_chars = [
        "✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n✪✨✪..**EMON-USERBOT**..✪✨✪\n✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n",
        "✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n✨✪✨..**EMON-USERBOT**..✨✪✨\n✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n",
        "✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n✪✨✪..**EMON-USERBOT**..✪✨✪\n✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n",
        "✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n✨✪✨..**EMON-USERBOT**..✨✪✨\n✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n",
        "✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n✪✨✪..**EMON-USERBOT**..✪✨✪\n✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n",
        "✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n✨✪✨..**EMON-USERBOT**..✨✪✨\n✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n",
        "✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n✪✨✪..**EMON-USERBOT**..✪✨✪\n✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n",
        "✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n✨✪✨..**EMON-USERBOT**..✨✪✨\n✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n",
        "✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n✪✨✪..**EMON-USERBOT**..✪✨✪\n✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n",
        "✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n✨✪✨..**EMON-USERBOT**..✨✪✨\n✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n",
        "✨✪✨✪✨✪✨✪✨✪✨\n✪✨✪✨✪✨✪✨✪✨✪\n✪✨✪..**EMON-USERBOT**..✪✨✪\n✪✨✪✨✪✨✪✨✪✨✪\n✨✪✨✪✨✪✨✪✨✪✨\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 192])  

            
    
@cilik_cmd(pattern="city(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event, 
        """☁☁🌞      ☁           ☁
       ☁  ✈         ☁    🚁    ☁    ☁        ☁          ☁     ☁   ☁
🏬🏨🏫🏢🏤🏥🏦🏪🏫
              🌲/     l🚍\🌳👭
           🌳/  🚘 l  🏃 \🌴 👬                       👬  🌴/            l  🚔    \🌲
      🌲/   🚖     l               \
   🌳/🚶           |   🚍         \ 🌴🚴🚴
🌴/                    |                     \🌲"""
    )        
  
  
@cilik_cmd(pattern="plane(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(14)
    event = await edit_or_reply(event, "Wait for plane...")
    animation_chars = [
        "✈-------------",
        "-✈------------",
        "--✈-----------",
        "---✈----------",
        "----✈---------",
        "-----✈--------",
        "------✈-------",
        "-------✈------",
        "--------✈-----",
        "---------✈----",
        "----------✈---",
        "-----------✈--",
        "------------✈-",
        "-------------✈",
   
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])  
  

@cilik_cmd(pattern="police(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(11)
    event = await edit_or_reply(event, "Police")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])  
        
        
CMD_HELP.update(
    {
        "animasi7": f"➢ **Plugin : **`animasi7`\
        \n\n ┌✪ **Syntax :** `{cmd}emon`\
        \n └✪ **Function : **Animasi Emon Userbot.\
        \n\n ┌✪ **Syntax :** `{cmd}city`\
        \n └✪ **Function : **Mengirim Gambar Kota.\
        \n\n ┌✪ **Syntax :** `{cmd}plane`\
        \n └✪ **Function : **Mengirim Gambar Animasi Pesawat.\
        \n\n ┌✪ **Syntax :** `{cmd}police`\
        \n └✪ **Function : **Mengirim Gambar Animasi Polisi.\
    "
    }
)
