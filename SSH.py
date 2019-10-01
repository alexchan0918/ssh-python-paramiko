import paramiko
import tkinter as tk
import sys


def gui():
    def Alex():
        username_entry.delete(0, 'end')
        username_entry.insert(0, 'alexchan')
        password_entry.delete(0, 'end')
        password_entry.insert(0, '')
        hostname_entry.delete(0, 'end')
        hostname_entry.insert(0, 'login.cpp.edu')
        port_entry.delete(0, 'end')
        port_entry.insert(0, '22')

    def Priscilla():
        username_entry.delete(0, 'end')
        username_entry.insert(0, 'pfluuvilla')
        password_entry.delete(0, 'end')
        password_entry.insert(0, '')
        hostname_entry.delete(0, 'end')
        hostname_entry.insert(0, 'login.cpp.edu')
        port_entry.delete(0, 'end')
        port_entry.insert(0, '22')

    def shell():
        global x
        x = 0

        # This method creates a SSH connection
        def sshConnect(hostname, port, username, password):
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(hostname, port, username, password)

        # This method sends a SSH command and writes the output
        def sshCommand(command):
            stdin, stdout, stderr = client.exec_command(command)
            shell_frame.insert('end', stdout.read())

        # This method will exit the client
        def quit():
            sys.exit()

        # This method will send the command to the shell and format the output
        def send():
            s = shell_entry.get()
            shell_frame.insert('end', ' ' + s + '\n')
            sshCommand(s)
            shell_frame.insert('end', username + '@' + hostname + " ~ $")
            shell_entry.delete(0, 'end')

        # This creates the window for the shell
        WIDTH = 700
        HEIGHT = 400
        root = tk.Toplevel(win)
        username = username_entry.get()
        hostname = hostname_entry.get()
        port = port_entry.get()
        password = password_entry.get()
        client = paramiko.SSHClient()
        sshConnect(hostname, port, username, password)

        # The following code formats the GUI for the shell
        root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
        root.title('Secure Shell ' + username + '@' + hostname)
        shell_frame = tk.Text(root)
        shell_frame.place(relx=0, rely=0, relwidth=1, relheight=.9)
        command_frame = tk.Frame(root)
        command_frame.place(relx=0, rely=.9, relwidth=1, relheight=.1)
        shell_entry = tk.Entry(command_frame)
        shell_entry.place(relx=0, rely=0, relwidth=.8, relheight=1)
        # The following code creates a button that will send a command when pushed
        command_button = tk.Button(command_frame, text='Send Command', command=send)
        command_button.place(relx=.6, rely=.0, relwidth=.2, relheight=1)
        # The following code creates a button that will quit the program when pushed
        quit_button = tk.Button(command_frame, text='Quit', command=quit)
        quit_button.place(relx=.8, rely=.0, relwidth=.2, relheight=1)
        shell_frame.insert('end', username + '@' + hostname + " ~ $")

    
    HEIGHT = 175
    WIDTH = 325
    # The following code creates the labels, buttons, menu, and main window
    win = tk.Tk()
    win.geometry(str(WIDTH)+'x'+str(HEIGHT))
    win.title("SSH Client")
    win.resizable(False, False)
    input_frame = tk.Frame(win)
    input_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.8, anchor='n')
    menu = tk.Menu(win)
    win.config(menu=menu)
    username_label = tk.Label(input_frame, text="Username:")
    password_label = tk.Label(input_frame, text="Password:")
    hostname_label = tk.Label(input_frame, text="Host Name:")
    port_label = tk.Label(input_frame, text="Port:")
    username_entry = tk.Entry(input_frame)
    password_entry = tk.Entry(input_frame, show="*")
    hostname_entry = tk.Entry(input_frame)
    default_port = tk.StringVar(input_frame, value='22')
    port_entry = tk.Entry(input_frame, textvariable=default_port)
    connect_button = tk.Button(input_frame, text="Connect", command=shell)
    filemenu = tk.Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Priscilla', command=Priscilla)
    filemenu.add_command(label='Alex', command=Alex)
    filemenu.add_command(label='Exit', command=win.quit)

    # The following code places the GUI items created
    username_label.grid(row=0, column=0, sticky='e')
    username_entry.grid(row=0, column=1)
    password_label.grid(row=1, column=0, sticky='e')
    password_entry.grid(row=1, column=1)
    hostname_label.grid(row=2, column=0, sticky='e')
    hostname_entry.grid(row=2, column=1)
    port_label.grid(row=3, column=0, sticky='e')
    port_entry.grid(row=3, column=1)
    connect_button.grid(row=4, column=1, sticky='e')

    win.mainloop()



def main():

    gui()

if __name__ == '__main__':
    main()
