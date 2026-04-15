# Import the necessary libraries  
from tkinter import *  # Import all modules from tkinter  
from tkinter import messagebox  # Import messagebox module from tkinter  
import base64  # Import base64 library for encoding and decoding  
import os  # Import os library for environment variables  
  
# Get the secret key from the environment variable 'SECRET_KEY'  
secret_key = os.environ.get('SECRET_KEY')  
  
# Create a new tkinter window  
screen = Tk()  
# Set the geometry of the window to 400x500 pixels  
screen.geometry("400x500")  
# Set the title of the window to "Shashank's_App"  
screen.title("Shashank's_App")  
  
# Define a function to decrypt the message  
def decrypt():  
   # Get the password from the code entry field  
   password = code.get()  
   # Check if the password is "2005"  
   if password == "2005":  
      # Create a new window for decryption  
      screen1 = Toplevel(screen)  
      # Set the title of the window to "decryption"  
      screen1.title("decryption")  
      # Set the geometry of the window to 400x200 pixels  
      screen1.geometry("400x200")  
      # Set the background color of the window to #00bd56  
      screen1.configure(bg="#00bd56")  
  
      # Get the message from the text1 entry field  
      message = text1.get(1.0, END)  
      # Encode the message to ASCII  
      encode_message = message.encode("ascii")  
      # Decode the encoded message using base64  
      base64_bytes = base64.b64decode(encode_message)  
      # Decode the base64 bytes to ASCII  
      encrypt = base64_bytes.decode("ascii")  
  
      # Create a label with the text "DECRYPT" in the new window  
      Label(screen1, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)  
      # Create a text field to display the decrypted message  
      text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)  
      # Place the text field in the new window  
      text2.place(x=10, y=40, width=380, height=150)  
  
      # Insert the decrypted message into the text field  
      text2.insert(END, encrypt)  
  
   # Check if the password is empty  
   elif password == "":  
      # Show an error message with the text "Input Password"  
      messagebox.showerror("decryption", "Input Password")  
  
   # Check if the password is not "2005"  
   elif password != "2005":  
      # Show an error message with the text "Invalid Password"  
      messagebox.showerror("decryption", "Invalid Password")  
  
# Define a function to encrypt the message  
def encrypt():  
   # Get the password from the code entry field  
   password = code.get()  
   # Check if the password is "2005"  
   if password == "2005":  
      # Create a new window for encryption  
      screen1 = Toplevel(screen)  
      # Set the title of the window to "encryption"  
      screen1.title("encryption")  
      # Set the geometry of the window to 400x200 pixels  
      screen1.geometry("400x200")  
      # Set the background color of the window to #ed3833  
      screen1.configure(bg="#ed3833")  
  
      # Get the message from the text1 entry field  
      message = text1.get(1.0, END)  
      # Encode the message to ASCII  
      encode_message = message.encode("ascii")  
      # Encode the encoded message using base64  
      base64_bytes = base64.b64encode(encode_message)  
      # Decode the base64 bytes to ASCII  
      encrypt = base64_bytes.decode("ascii")  
  
      # Create a label with the text "ENCRYPT" in the new window  
      Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)  
      # Create a text field to display the encrypted message  
      text2 = Text(screen1, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)  
      # Place the text field in the new window  
      text2.place(x=10, y=40, width=380, height=150)  
  
      # Insert the encrypted message into the text field  
      text2.insert(END, encrypt)  
  
   # Check if the password is empty  
   elif password == "":  
      # Show an error message with the text "Input Password"  
      messagebox.showerror("encryption", "Input Password")  
  
   # Check if the password is not "2005"  
   elif password != "2005":  
      # Show an error message with the text "Invalid Password"  
      messagebox.showerror("encryption", "Invalid Password")  
  
# Define a function to reset the fields  
def reset():  
   # Clear the code entry field  
   code.set("")  
   # Clear the text1 entry field  
   text1.delete(1.0, END)  
  
# Create a label with the text "Type text for Encryption and Decryption"  
Label(text="Type text for Encryption and Decryption", fg="black", font=("italic", 15)).place(x=10, y=10)  
# Create a text field to input the message  
text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)  
# Place the text field in the window  
text1.place(x=10, y=50, width=355, height=300)  
  
# Create a label with the text "Enter key for encryption and decryption"  
Label(text="Enter key for encryption and decryption", fg="black", font=("italic", 15)).place(x=10, y=170)  
  
# Create a string variable to store the password  
code = StringVar()  
# Create an entry field to input the password  
Entry(textvariable=code, width=19, bd=0, font=("*", 25), show="").place(x=10, y=200)  
  
# Create a button to encrypt the message  
Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)  
# Create a button to decrypt the message  
Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)  
# Create a button to reset the fields  
Button(text="RESET", height="2", width=47, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)  
  
# Start the main event loop of the application  
screen.mainloop()