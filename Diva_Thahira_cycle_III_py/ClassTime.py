class time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second=second
    def __add__(self,other):
        tot_sec=((self.__hour*60*60)+(self.__minute*60)+self.__second)+((other.__hour*60*60)+(other.__minute*60)+other.__second)
        hours=tot_sec//3600
        minutes=(tot_sec%3600)//60
        seconds=tot_sec%60
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
time1=time(12,30,0)
time2=time(2,45,0)
print(time1+time2)

