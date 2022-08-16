from mirai import GroupMessage

@bot.on(GroupMessage)
def on_group_message(event: GroupMessage):
    if str(event.message_chain) == '你好':
        return bot.send(event, 'Hello, World!')