import tkinter as tk
from AIchat import callAI

def send_message(event):
    message = entry.get()
    if message:
        # Display user's message
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "AOYANMA: " + message + "\n")
        chat_display.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

        # Process on this 
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, "IROHA: " + callAI(message) + "\n")
        chat_display.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Chat Program")

image_path = "D:\\voicevox_and_chai\\img\\iroha.png"

# Load the image file from disk.
icon = tk.PhotoImage(file=image_path)
# Set it as the window icon.
root.iconphoto(True, icon)

# Load your image
image = tk.PhotoImage(file=image_path)

# Create a label to display your image on the left side
image_label = tk.Label(root, image=image)
image_label.grid(row=0, column=0, rowspan=2, padx=10, pady=10)

# Create text area for displaying chat
chat_display = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
chat_display.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# Create a label for the entry
entry_label = tk.Label(root, text="Text to Input:")
entry_label.grid(row=1, column=1, padx=10, pady=10, sticky=tk.E)

# Create entry for typing messages
entry = tk.Entry(root, width=60)
entry.grid(row=1, column=2, padx=10, pady=10)

# Bind the Enter key to send_message function
entry.bind('<Return>', send_message)

# Start the Tkinter event loop
root.mainloop()
