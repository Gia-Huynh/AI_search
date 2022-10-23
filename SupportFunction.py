import numpy as np
gay_dict = {'x': 0, ' ': 1, 'S': 2, 's': 2, '+': 3}
def ReadFile (filename):
    #0.........x
    #.
    #.
    #y
    with (open(filename, "r")) as f:
        bonusP = []
        forceP = []
        gay_map = []
        exit_x = -1
        exit_y = -1
        start_x = 0
        start_y = 0
        gay = f.readline()
        n = int (gay)
        
        for i in range (0, n):
            gay = f.readline().split()
            if (gay[2] == "0"):
                forceP.append ([int (n) for n in gay[0:2]])
            else:
                bonusP.append ([int (n) for n in gay[0:3]])
        gay = f.readline().rstrip('\r\n')
        while(gay != ''):
            map_line = [gay_dict[t] for t in gay]
            gay_map.append (map_line)
            gay = f.readline().rstrip('\r\n')
            try:
                start_x = map_line.index(2)
                start_y = len(gay_map)-1
            except:
                pass
        try:
            exit_x = gay_map[len(gay_map)-1].index(1)
            exit_y = len(gay_map)-1
        except:
            try:
                exit_x = gay_map[0].index(1)
                exit_y = 0
            except:
                try:
                    inverse_gay_map = list(zip (*gay_map))
                    exit_y = inverse_gay_map[0].index(1)
                    exit_x = 0
                except:
                    try:
                        exit_y = inverse_gay_map[len(inverse_gay_map)-1].index(1)
                        exit_x = len(inverse_gay_map)-1
                    except:
                        #print ("Can not find exit location")
                        pass

        return gay_map, bonusP, forceP, start_x, start_y, exit_x, exit_y
