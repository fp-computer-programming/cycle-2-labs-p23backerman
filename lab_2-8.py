from statistics import median_low


points=15
if points <= 8:
        print('No medal')
else:
        if points <= 11:
                print('bronze medal')
        else: 
                if points < 15:
                        print('silver medal')
                else:
                                print('GOLD MEDAL!!!')

