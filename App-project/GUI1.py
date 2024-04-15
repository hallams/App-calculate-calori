from tkinter import Tk, Label, Button, Entry, messagebox, Toplevel
import json



# def anderesite():
#     Windows2=Toplevel()
#     Windows2.title("Bericht")
#     Windows2.geometry("300x400")
    


windows = Tk()
windows.title("personliche site")
windows.geometry("300x400")


# Function to handle button click and save user information



def save_info():
        user_name = name_entry.get()
        user_weight = weight_entry.get()
        user_height = height_entry.get()
        user_age = age_entry.get()
        user_gender = gender_entry.get()
        user_activity_level = activity_entry.get()

        user_info = {
            user_name: {
                'weight': user_weight,
                'height': user_height,
                'age': user_age,
                'gender': user_gender,
                'activity_level': user_activity_level
            }
        }

        # Save the user's information to a JSON file
        with open("userdata.json", "w") as file:
            json.dump(user_info, file)
        
        # Show a message box to confirm information saved
        messagebox.showinfo("Info", "User information saved successfully!")


# Create labels and entry fields for user input
name = Label(windows, text="name")
name.pack()
name_entry = Entry(windows)
name_entry.pack()

weight = Label(windows, text="weight")
weight.pack()
weight_entry = Entry(windows)
weight_entry.pack()

height = Label(windows, text="height")
height.pack()
height_entry = Entry(windows)
height_entry.pack()

age = Label(windows, text="age")
age.pack()
age_entry = Entry(windows)
age_entry.pack()

gender = Label(windows, text="gender")
gender.pack()
gender_entry = Entry(windows)
gender_entry.pack()

activity_level = Label(windows, text="Enter your activity level: \n l active/m active/v active):")
activity_level.pack()
activity_entry= Entry(windows)
activity_entry.pack()





# Create a button to save user information
button01 = Button(windows, text="Save", command=save_info)
button01.pack()




status = Label(windows, text="")
status.pack()



windows.mainloop()




