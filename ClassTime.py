class time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def __add__(self,other):
        tot_seconds=((self.__hour*60*60)+(self.__minute*60)+self.__second)+((other.__hour*60*60)+(other.__minute*60)+other.__second)
        hours=(tot_seconds//3600)%24
        minutes=(tot_seconds%3600)//60
        seconds=tot_seconds%60
        
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
time1=time(20,30,12)
time2=time(3,45,15)

print(time1+time2)