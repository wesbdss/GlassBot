# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 01:27:32 2019

@author: wesbdss
"""

import websocket
import json


def receive(ws):
    while True:
        result = ws.recv()
        if result.count("message"):
            return result
        else: pass
def sendResponse(txt):
    msg = '{"type":"message","value":"'+txt+'","username":"GlassBot","idCliente":1,"clientcolor":"#ffffff"}'
    ws.send(msg)

    

uri = "ws://localhost:5001"
init = '{"username":"GlassBot"}'
imagem = '{"type":"message","value":"","username":"Glassbot","idCliente":2,"clientcolor":"#3bb1a4","image":"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAllBMVEVB/80AMW9C/89D/9EAJmwAKGwAK2043rwAFmgAImsAGmkAI2sYeY4opp8koKEqtKkikpczzbQPYIUww64gjJMprqUALm4tv68XdIsQZIcAHWoz0LY/+Moei5Ycfo8lpaIch5Y77MQAAGULTnsAFGkFO3MUaYc878Y227sHRHcGQHYOWYAjmZwWbogCNnEsuqwKSnkAC2a3xUa7AAAHiklEQVR4nO2daXuyOhBAYYDUpa5oUMSFurWVqvf//7kLtkCQ4AZC4jvnU58YKcdBEiaLioIgCIIgCIIgCIIgCIIgCIIgCIIgCIIgyD8BaBFwrULJp1YM8Nlt/+G98RTB8sLX227pp1cE0LXrzRMfJs9QG9V+X7ZXFj/IwuN0a+oJm2/4bpxepcZQzqs0oEuuG1JV1gj6gOM1rhlS0pE3ggFTnV40pGpH3gieAM+4ZEgNS+4I+oYwrWUbUn0oeQQDwCONDMMmMWWPYACAl9EevtsyNhPAY2pqnFJtceAVi37ZdlocvC6vtDUb8krNqhUuAt06D13nFhu8Qnt/EDiKMGiquaGrQ9UemWgDg+Y3VOle1G4cDOwC/AJFW8x+DgyMYgR9RSpkFLv1ogQF7a0O9OIEfcWGVbXQGVpXL+ImwygKdrtxBgVeon+KQjUa2pSwJ0ea3Ab+Ok32OvCjWLVXhDZvsIL6uP0g3pH9pKj9KcqF6n8JWcGdqz3KZM0q1npCGupjbnL0NmCyZxQbQhrqu22e04LJFxHbkPRzRDAAJobYhkbu1GCYJxbWMHdeAkZoWAFoeBdoWAloeBdoWAnZhuA4zsUkNvg1lEQFqQxBsRb9fneS+UaAw6I/TlaQytCZGjohzb2XceXCdqEHFdZz9mORyXBgn57ZaSMrcTb7TbDSDyYnI5EhuOQvKUH6Lnc+zVuY3CHjbVwqj6E2j1LgOvdUNS80pPu4gkyG06g0Ywx4FlXQTSkN21GGscmPYTccqaKqlDGEz/AqJUv+vLZJLaywc2U0VJzRXxBtj3+mzvgviLW2lPdS/2b6EzQXRJ9lnCi4m1MFYyZrewjb+XHV2HWcrDeC632t7J3FVpDKUPntkl44TU4FuQwfQUxD7+UNXz+GaHgPaFgJaHgXaFgJaHgXohuSlzfMH0PtR2xDevzMpwiW4OP4KtnnmqoAB5UKbqiSZY6ZTJrFCIpqqBLy+eiUKDgkplGLMycKDv+xJ0aW3QeZfieOQ3LOzSkQbagmZhXqj5IQ/JoII+gzLHgCrS9Ie0ItGYKiFck3dySgQiB5oeYWVCdCRfDEcFWcIlFFXLanFRdF8i1gBAOGjWIUCRUxggHakBahSL6EaenTDEl+RSFvMjGtJrkC8xFQ3uvGt6iX6C9gdq6wieZx69MDr0LOx6+nA9c61/Hovm1xK4j7HbwR1lB6GS5oKD9oKD9oKD+vZMhv8uMV0bbJFD923Eo/IoDpO49l1DEl46hwNLz9uE58rB/uvNWS8E+kbvBget4kLl3Nbz2uu7Gjd31UmG4ELR5CugVKWrcd1xkzx61VZwjO6M49MmjNu+W47o7dPaU6Q1De74rgCf36dxG2m8RxKzOEaGbpXVHUr0URtrvk1hRVGYIz0zMsLlO7HEX/JnN23IoMQRk9uAkIJZfuqODszi/9agyDZuIxweB2k60I7ji1RVMlhvc2E2eKJGsPPnA26eNWYnjWTJAb9vtIDMxlNBr+TSaKYLxFWCUtfitxidY35lWsYyI4dd6oIdtMNNvxWzNnkD8Rj/2y6O9b7q56ya333MSOJjrnicO/ycQ3r8YkPmYFggnD+o9zyznA29K4aJhsJqqev8AY6rd2/cFVyQVDcPrsdSyOofFz8y4n2tuOZhqC2080E+IY1u+ZABY/F58bppqJVzNM9UVfzfD8aeLlDMFZpnoyL2XoNxPp7UKfYcjfAZdfWqghk7JgZiwW3+KDNYpyYsx63Q6vtFBD7T3q4+7H+/BPsik816Z5tTC5VWvFy3wHjShRNnySIfOYYs2j6Tqk8Fyb1uaddbxO2S99uiE1YZ6e6FHU05MYhpoyX722oV/qnW9T/HKGZw+fr2iodGuJKL6gIcwTG6W+oKECbXaO5ysaKgobxcIMo11W1HonHp2MXewSDQHmH42Qolp86NnhlUF3o4hoqJPdmeT5MVSUSUSvqFybZq0jm/RQZ0KwDMOn/BSGZWfOGyXNxG/hlGD4FDRznaFIvpPLImQ19KPIn6ZO9LN/La8hmDxFsj7/z/Ia+s/B6QuVpjfxkthQUczzxQZUTf/gltSG2lkU6Zqz9kpqQ/92wy7fIk3efy3AMO4Ylm/INhqUv+4jt6FxCLYEPaGUb6hALNDk72iZ25BuZiGLr/DzNPg7vj0BGMad8PlzDNnZblF2bV3acDa0nm+YJtfy8DupxJCoJU5IqMKQLN9KXCdUgaHxXepvsZRvSI7lzpkp3dAo8SZzomzDnPuIPEDJhn4zUfZiRGhFI3r1FnexQZx5tDvcChlrFOIEWkyNlv+DT9CLc1LHMY9j1A85Lvq30+pxMHP97NCjimacWby4zJesJ4v6tTXBETb3x2armbcGmTmp5DdInWiL26cKn2d7KgV6N+zxQb5MTVpDBayr+wqQYI91eQ39KO4vK5KvYM8AiQ39KGanwAPB/el8ZTZkGw2O4Pp31wepDdlGIyUYbg4ktyE3P/wrqIYz0SU3DBqNVS3NKh6o0WYfnAp8PgQ0VOCNixtXcPk1uFSxrOAqGYsLrlYQpnuGIAiCIAiCIAiCIAiCIAiCIAiCIMg/xv+bBs4jALUG/AAAAABJRU5ErkJggg=="}'
msg0 = '{"type":"message","value":"Olá meu nome é Glassbot! Sou atendente do Goiás Transparente e estou aqui para facilitar seu acesso.","username":"GlassBot","idCliente":2,"clientcolor":"#ffffff"}'

#msg = '{"type":"message","value":"texto","username":"GlassBot","idCliente":2,"clientcolor":"#ffffff"}'
ws = websocket.create_connection(uri)
ws.send(init)
ws.send(imagem)
ws.send(msg0)
result = receive(ws)
print("RECEBEU: %s" % result)


#Parte do chat bot agr

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

#while True:
    #sendResponse(kernel.respond(receive(ws)))
ws.close()

