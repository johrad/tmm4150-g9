from config import server_ip, server_username, path_server
import subprocess

def send(filepath):    
    try:
        # subprocess.Popen(['scp', 'data.json', f'{server_username}@{server_ip}:/home/data'])
        subprocess.Popen(['scp', filepath, f'{server_username}@{server_ip}:/home/data'])
    except Exception as e:
        print("ERROR!! ", e)




