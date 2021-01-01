from datetime import datetime
import sys
import calendar

first_arg = sys.argv[1]       
def send(fsm=first_arg):
    try:
        currentyear=datetime.now().year
        curmonth=datetime.now().month
        if curmonth < int(fsm):
            fsy=str(currentyear-1)
            fey=str(currentyear)
        else:
            fsy=str(currentyear)
            fey=str(currentyear+1)
        print("fsy",fsy)
        print("fey",fey)
        fsd=datetime.strptime('1/'+str(fsm)+'/'+fsy, '%d/%m/%Y').date()
        print("fsd",fsd)
        fem=int(fsm)+11-12
        print("fem",fem)
        flday=calendar.monthrange(int(fey),fem)[1]
        print("flday",flday)
        fed=datetime.strptime(str(flday)+'/'+str(fem)+'/'+fey, '%d/%m/%Y').date()
        print("fed",fed)
        print("Done")
    except Exception as e:
        print("Issue")
if __name__ == "__main__":
    send()