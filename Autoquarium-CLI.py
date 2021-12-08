import serial # pip install pyserial
import time
import os
import stdiomask # pip install stdiomask


#arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
version = "0.0.1"

connect_key = "blub-blub-blub\r\n"
confirm_key = "hello-fish"


# Instructions
get_input = "GETIN\r\n"
clear_screen = "CLRSCR\r\n"
exit_cli = "EXIT\r\n"
get_pass = "GETPS\r\n";



def printWelcome():
    print("");
    print("-----------------------------------------------------------------");
    print("               _                               _                 ");
    print("    /\\        | |                             (_)                ");
    print("   /  \\  _   _| |_ ___   __ _ _   _  __ _ _ __ _ _   _ _ __ ___  ");
    print("  / /\\ \\| | | | __/ _ \\ / _` | | | |/ _` | '__| | | | | '_ ` _ \\ ");
    print(" / ____ \\ |_| | || (_) | (_| | |_| | (_| | |  | | |_| | | | | | |");
    print("/_/    \\_\\__,_|\\__\\___/ \\__, |\\__,_|\\__,_|_|  |_|\\__,_|_| |_| |_|");
    print("                           | |                                  ");
    print("                           |_|                                  ");
    print("CLI tool")
    print("version: "+ version);
    print("-----------------------------------------------------------------");

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# triggers the enterence into the CLI
def startup():
    while True:
        data_in = arduino.readline()
        data = str(data_in.decode("utf-8"))
        if data == connect_key:
            arduino.write(bytes(confirm_key, 'utf-8'))
            return



def password_input():
    passwrd = stdiomask.getpass(prompt='')
    write(passwrd)
    read_all()


def read_all():
    data = ""
    while True:
        data_in = arduino.readline()
        data = str(data_in.decode("utf-8"))
        if data == get_input:
            return
        elif data == get_pass:
            password_input()
        elif data == clear_screen:
            clearScreen();
            printWelcome();
        elif data == exit_cli:
            exit();
        elif data == connect_key:
            continue
        else:
            print(data, end="")


def write(x):
    x_str = str(x)
    ret = arduino.write(bytes(x_str, 'utf-8'))
    time.sleep(0.05)



# main
#read_all() # make this work better
arduino = serial.Serial()
print("Please connect Autoquarium to computer")
while True:
    try:
        arduino = serial.Serial(port='COM8', baudrate=115200, timeout=.1)
    except:
        continue
    else:
        break

print("Connecting to Autoquarium...")
startup()
print("Connected")

read_all()

while True:
    option = input("><{{*> ")
    write(option)
    read_all()
