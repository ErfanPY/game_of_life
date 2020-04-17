from game_of_life import *

h,w = 40, 40


def add_pat_test ():
    u = universe(h, w)  

    pattern = {'Glider':[[0, 1, 0], [0, 0, 1], [1, 1, 1]],
               'Road':
    [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
     [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
     ]          
    }
    u.clear()
    u.add_pat(pattern['Glider'])
    u.add_pat(pattern['Road'], 10,10)
    u.draw()
    input('to start Evolution press enter')

    while True :
        u.draw()
        u.evolution()
        time.sleep(1)
        
def asci_to_pat_test ():
    """
    use this site to make asci arts :
    http://www.patorjk.com/software/taag/
    """
    erfan = """
  ______   _____    ______              _   _ 
 |  ____| |  __ \  |  ____|     /\     | \ | |
 | |__    | |__) | | |__       /  \    |  \| |
 |  __|   |  _  /  |  __|     / /\ \   | . ` |
 | |____  | | \ \  | |       / ____ \  | |\  |
 |______| |_|  \_\ |_|      /_/    \_\ |_| \_|
                                              
                                    
    """

    u = universe(40, 40)

    u.clear()
    u.add_pat(u.asci_to_pat(erfan), 15, 0)
    u.draw()
    input('to start Evolution press enter')

    while True :
        u.draw()
        u.evolution()
        time.sleep(0.1)
        
def loop_test ():
    'renew the world every 10 second'
    u = universe(h, w)
    u.draw()
    input('to start Evolution press enter')
    while 1:
        for i in range(100):
            u.draw()
            u.evolution()
            time.sleep(0.1)
            
        pat = [['*']*h]*w
        u.add_pat(pat)
        u.draw()
        time.sleep(1)
        u = universe(h, w)

add_pat_test()

