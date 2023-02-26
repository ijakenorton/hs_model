import sys    
def main():
    print('help')
    file = 'Power.log'
    # if len(sys.argv) < 2:
    #     file = 'log_example.txt'
    # else:
    #     file = sys.argv[1]
    
        
    with open(file, "r", encoding='utf-8') as f:
        for i in range(1500):
            
            line = f.readline()
            if line:
                split_line = line.split(" ")
                remove_empty = [element for element in split_line if element != ""]
                if 'tag=PLAYER_LEADERBOARD_PLACE' and 'zone=SETASIDE' in remove_empty:
                    print(remove_empty)
            
            
            
if __name__ == "__main__":
    main()