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

uri = "ws://localhost:5001"
init = '{"username":"GlassBot"}'
msg0 = '{"type":"message","value":"Olá meu nome é Glassbot! Sou atendente do Goiás Transparente e estou aqui para facilitar seu acesso.","username":"GlassBot","idCliente":2,"clientcolor":"#ffffff"}'
msg1 = '{"type":"message","value":"Hoje eu sou capaz de:","username":"GlassBot","idCliente":2,"clientcolor":"#ffffff"}'
msg2 = '{"type":"message","value":"-> Fazer busca:","username":"GlassBot","idCliente":2,"clientcolor":"#ffffff"}'
msg = '{"type":"message","value":"Comi sua Mae","username":"GlassBot","idCliente":2,"clientcolor":"#ffffff"}'
ws = websocket.create_connection(uri)
ws.send(init)
result = receive(ws)
print("Received '%s'" % result)
#date = json.loads(result)
#print(date['value'])
ws.send(msg)


#Parte do chat bot agr

import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    kernel.respond(input("Enter your message >> "))
ws.close()

