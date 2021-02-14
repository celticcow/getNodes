#!/usr/bin/python3

import json
import requests

def getExitNodes():
    debug = 1

    headers = {"Accept" : "application/json"}
    url = "https://check.torproject.org/exit-addresses"

    exit_list = list()

    try:
        response = requests.get(url, headers=headers)

        if(response.status_code == 200):
            info = response.text.split('\n')

            for line in info:
                if('ExitAddress' in line):
                    just_ip = line.split(' ')[1]
                    exit_list.append(just_ip)
                    if(debug == 1):
                        print(line)
                        print(just_ip)
        else:
            print("Non 200 return code")
    except:
        print("could not pull list")
    
    return(exit_list)
#end of getExitNodes

def main():
    print("Get Nodes")

    exit_list = getExitNodes()

    print(exit_list)
    print(len(exit_list))
#end of main


if __name__ == "__main__":
    main()
#end