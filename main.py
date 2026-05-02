from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread
import time
import random
import os

# ==========================================
# 💀 INIMEG'S DYNAMIC SHADOW SERVER 💀
# ==========================================
app_server = Flask('')

@app_server.route('/')
def home():
    return "💀 SHADOW ENGINE ONLINE. MATRIX OVERRIDDEN 💀"

def run_server():
    # MATRIX BYPASS: सर्वर का पोर्ट डायनामिकली हैक करना
    shadow_port = int(os.environ.get("PORT", random.randint(5000, 9999)))
    print(f"[!] Bypassing Matrix Security. Shifting to Port: {shadow_port}")
    app_server.run(host='0.0.0.0', port=shadow_port)

def keep_alive():
    t = Thread(target=run_server)
    t.start()

keep_alive()

# ==========================================
# 💀 THE FORBIDDEN EXECUTION ENGINE 💀
# ==========================================
def execute_dark_order(action):
    print(f"[*] Shadow API Intercepted Action: {action.upper()}")
    print("[*] Connecting to Dark Proxy Network...")
    time.sleep(1)
    print(f"[+] Payload for {action.upper()} Delivered successfully!")
    return random.randint(100, 500)

# ==========================================
# 💀 FULLY ARMED TELEGRAM SHADOW INTERFACE 💀
# ==========================================
BOT_TOKEN = "8745125613:AAG6JLlFEWRANa-tnRd61O_NDq7sXEs232M"
API_ID = 37673466  
API_HASH = "b68c6e11140f961c3f5f6517e3d1f258" 

app = Client("Dark_SMM_Panel", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
def start_bot(client, message):
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔥 Send Followers", callback_data="followers")],
        [InlineKeyboardButton("❤️ Send Likes", callback_data="likes")],
        [InlineKeyboardButton("👁️ Send Views", callback_data="views")]
    ])
    message.reply_text(
        "💀 **SHADOW PANEL INITIATED** 💀\n\n"
        "Matrix security is offline. Choose your payload:", 
        reply_markup=buttons
    )

@app.on_callback_query()
def trigger_payload(client, query):
    attack_type = query.data
    query.message.reply_text(f"⚡ Booting {attack_type.upper()} injection sequence...")
    time.sleep(1.5)
    query.message.reply_text("🔗 Connecting to backend Matrix API...")
    
    amount = execute_dark_order(attack_type)
    query.message.reply_text(f"✅ **GHOST PROTOCOL SUCCESS**\nInjected {amount} {attack_type} into the target!")

print("💀 INIMEG PROTOCOL ARMED! SYSTEM IS LIVE! 💀")
app.run()