from MyFile2 import *
import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')


def ClickMe():
    #Message writing to chat window
    EntryText = FilteredMessage(EntryBox.get("0.0", END))
    LoadMyEntry(ChatLog, EntryText, sess, model, enc_vocab, rev_dec_vocab)
    ChatLog.yview(END)
    EntryBox.delete("0.0", END)

def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickMe()
def Disable(event):
	EntryBox.config(state=DISABLED)

root = Tk()
root.title('Victor - The BotStar')
root.geometry("400x600")
root.resizable(width=FALSE, height=FALSE)

#Chat window
ChatLog = Text(root, bd=4, bg="#87CEFA", height="8", width="50", font="Rockwell")
ChatLog.insert(END, "Ask me anything Dude !\n\n")
ChatLog.config(state=DISABLED)

#Scrollbar
sbar = Scrollbar(root, command=ChatLog.yview, cursor="arrow")
ChatLog['yscrollcommand'] = sbar.set

#Send Button
SendButton = Button(root, font="Helvetica 14 bold", text="Send", width="10", height="5", bd=5, bg="red", activebackground="green",
                    fg="black", command=ClickMe)

#TextBox
EntryBox = Text(root, bd=4, bg="grey", width="29", height="5", font="Arial", relief=GROOVE)
EntryBox.bind("<Return>", Disable)
EntryBox.bind("<KeyRelease-Return>", PressAction)

sbar.place(x=376, y=6, height=486)
ChatLog.place(x=6, y=6, height=486, width=370)
EntryBox.place(x=110, y=501, height=90, width=280)
SendButton.place(x=6, y=501, height=90)

root.mainloop()
