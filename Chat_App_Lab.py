import paho.mqtt.client as paho
import tkinter as tk
from tkinter import messagebox
import json

broker = 'pldindustries.com'
port = 1883
username = 'app_client'
password = 'app@1234'

window = tk.Tk()
window.title("Client")
client_id = ""
topic = ""


topFrame = tk.Frame(window)
lblName = tk.Label(topFrame, text="Name:").pack(side=tk.LEFT)
entName = tk.Entry(topFrame)
entName.pack(side=tk.LEFT)
lblTopic = tk.Label(topFrame, text="Topic:").pack(side=tk.LEFT)
entTopic = tk.Entry(topFrame)
entTopic.pack(side=tk.LEFT)
btnConnect = tk.Button(topFrame, text="Connect", command=lambda: connect())
btnConnect.pack(side=tk.RIGHT)
topFrame.pack(side=tk.TOP)

displayFrame = tk.Frame(window)
scrollBar = tk.Scrollbar(displayFrame)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay = tk.Text(displayFrame, height=20, width=55)
tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
tkDisplay.tag_config("tag_your_message", foreground="blue")
scrollBar.config(command=tkDisplay.yview)
tkDisplay.config(yscrollcommand=scrollBar.set, background="#F4F6F7",
                 highlightbackground="grey", state="disabled")
displayFrame.pack(side=tk.TOP)


bottomFrame = tk.Frame(window)
tkMessage = tk.Text(bottomFrame, height=1, width=55)
tkMessage.pack(side=tk.LEFT, padx=(5, 13), pady=(5, 10))
tkMessage.config(highlightbackground="grey", state="disabled")
tkMessage.bind(
    "<Return>", (lambda event: getChatMessage(tkMessage.get("1.0", tk.END))))
bottomFrame.pack(side=tk.BOTTOM)


def connect():
    global username, client
    if len(entName.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter your name")
    if len(entTopic.get()) < 1:
        tk.messagebox.showerror(
            title="ERROR!!!", message="You MUST enter topic")
    else:
        global client_id, topic
        client_id = entName.get()
        topic = entTopic.get()
        entName.config(state=tk.DISABLED)
        entTopic.config(state=tk.DISABLED)
        btnConnect.config(state=tk.DISABLED)
        tkMessage.config(state=tk.NORMAL)

        # Connect to the Mqtt broker
        # Subscribe to the given topic


def receive_msg(client, userdata, message):
    msg = message.payload.decode("utf-8")

    # update the display when msg is recived
    # Use following function to update display of the GUI
    # update_display(""Name"", "Msg to send")


def getChatMessage(msg):
    msg = msg.replace('\n', '')

    # Use this function to publish msg when msg is enterd from GUI


def update_display(name, msg):
    texts = tkDisplay.get("1.0", tk.END).strip()
    tkDisplay.config(state=tk.NORMAL)
    if len(texts) < 1:
        tkDisplay.insert(tk.END, str(name)+"->"+msg)
    else:
        tkDisplay.insert(tk.END, "\n\n"+str(name)+"->"+msg)

    tkDisplay.config(state=tk.DISABLED)
    tkDisplay.see(tk.END)


window.mainloop()
