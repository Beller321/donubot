# @greyyvbss

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import cilik_cmd, edit_or_reply


@cilik_cmd(pattern="thanks(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
        "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
        "╔══╦╗────╔╗─╔╗╔╗\n"
        "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
        "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
        "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
        "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
        "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@cilik_cmd(pattern="malam(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "╔═╦═╦╗╔═╦══╦═╦══╗\n"
        "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
        "╠═║═╣╚╣║║║║║║║║║\n"
        "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
        "╔══╦═╦╗╔═╦══╗\n"
        "║║║║╬║║║╬║║║║\n"
        "║║║║║║╚╣║║║║║\n"
        "╚╩╩╩╩╩═╩╩╩╩╩╝")


@cilik_cmd(pattern="rumah(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "**GAMBAR RUMAH**\n"
        "╱◥◣\n"
        "│∩ │◥███◣ ╱◥███◣\n"
        "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
        "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
        "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
        "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@cilik_cmd(pattern="join(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "_/﹋\\_\n"
        "(҂`_´)\n"
        "<,︻╦╤─ ҉\n"
        "_/﹋\_\n"
        "\n**sini kebio gua teemoh njing😡**")
    
    
@cilik_cmd(pattern="lari(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "──▄█▀█▄─────────██\n"
        "▄████████▄───▄▀█▄▄▄▄\n"
        "██▀▼▼▼▼▼─▄▀──█▄▄\n"
        "█████▄▲▲▲─▄▄▄▀───▀▄\n"
        "██████▀▀▀▀─▀────────▀▀\n"
        " **LARI IPINN**\n")
    
    
@cilik_cmd(pattern="mobil(?: |$)(.*)")
async def _(event):
    await edit_or_reply(
        event,
        "──────▄▌▐▀▀▀▀▀▀▀▀▀▀▀▀▌\n"
        "───▄▄██▌█░░░░░░░░░░░░▐\n"
        "▄▄▄▌▐██▌█░░░░░░░░░░░░▐\n"
        "███████▌█▄▄▄▄▄▄▄▄▄▄▄▄▌\n"
        "▀❍▀▀▀▀▀▀▀❍❍▀▀▀▀▀▀❍❍▀\n")
    
      
CMD_HELP.update(
    {
        "animasi5": f"➢ **Plugin : **`animasi5`\
        \n\n ┌✪ **Syntax :** `{cmd}thanks`\
        \n └✪ **Function : **Kata-kata Thanks You.\
        \n\n ┌✪ **Syntax :** `{cmd}malam`\
        \n └✪ **Function : **Mengirim Gambar Selamat Malam.\
        \n\n ┌✪ **Syntax :** `{cmd}rumah`\
        \n └✪ **Function : **Mengirim Gambar Rumah.\
        \n\n ┌✪ **Syntax :** `{cmd}join`\
        \n └✪ **Function : **Mengirim Gambar Join Di Bio.\
        \n\n ┌✪ **Syntax :** `{cmd}lari`\
        \n └✪ **Function : **Mengirim Gambar Lari Ipin.\
        \n\n ┌✪ **Syntax :** `{cmd}mobil`\
        \n └✪ **Function : **Mengirim Gambar Mobil Optimus.\
    "
    }
)
