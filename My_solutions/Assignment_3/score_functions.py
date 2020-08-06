def batting_score(r,b,four,six):
    "Function for calculating batting score"
    strike_rate=r/b
    total_bat=r/2+four+2*six
    if r in range(50,100):
        total_bat=total_bat+5
    elif r>=100:
        total_bat=total_bat+10
        
    if strike_rate in range(80,100):
        total_bat=total_bat+2
        
    elif strike_rate>100:
        total_bat=total_bat+4
       

    return int(total_bat)


def bowling_score(w,o,r,f):
    "Functiion to calculate bowling score"
    total_bowl=10*w+10*f
    eco_rate=r/o 
    if w>=3:
        total_bowl=total_bowl+5
        
    elif w>=5:
        total_bowl=total_bowl+10
      
    if eco_rate>=3.5 and eco_rate<4.5:
        total_bowl=total_bowl+4
       
    elif eco_rate>=2 and eco_rate<3.5:
        total_bowl=total_bowl+7
        
    elif eco_rate<2:
        total_bowl=total_bowl+10
        
    
    return int(total_bowl)




        
    
    
