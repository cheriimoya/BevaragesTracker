import json
from time import sleep
from pdb import set_trace
import plotTotal as pT
import entries as et
import urllib.request

#WEBSERVER_PATH = 'http://192.168.1.21:8000/'
WEBSERVER_PATH='http://www2.hs-esslingen.de/~mahait13/'

def main():
    owe_list_old = []

    while(True):
        try:
            with urllib.request.urlopen(
                    WEBSERVER_PATH + "entries.json") as json_entries:
                entries = json.loads(json_entries.read().decode())
            with urllib.request.urlopen(
                    WEBSERVER_PATH + "persons.json") as json_persons:
                persons = json.loads(json_persons.read().decode())
        except:
            entries = []
            persons = []
        
        id_list = et.from_json(entries, persons)
        owe_list = [obj.owes_total for obj in id_list]

        # check after sleep if list is new
        if owe_list != owe_list_old and entries:
            # plot graph for specific drinks
            pT.plot_specific_drink(id_list, 'Oetti Export')
            pT.plot_specific_drink(id_list, 'Kaffee')

            # plot graph for liters 
            pT.plot_liters(id_list)
            pT.plot_liters_detailed(id_list)

            # plot graph for total owes 
            pT.plot_total_owe_list(id_list)
            
            # set new list to old list
            owe_list_old = owe_list
        else:
            sleep(5)


if __name__ == '__main__':
    main()
