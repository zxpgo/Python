import urllib2
import datetime
def toDate(date):# 对网站请求所需的绝对日期date 进行相对转换
date=datetime.date.today()-datetime.timedelta(8)
DGo=date0+datetime.timedelta(date)
DATE="%02d"%int(DGo.month)+"%02d"%int(DGo.day)
return DATE
def urlString(date, item):# 生成请求URL
return
"http://v.kuaidadi.com/point?cityId=310100&scope=city&date="+str(date)+"&dimension="+it
em+"&num=300"
def get_page(date, item):
# date:int 0~(-100)
# item:string 'distribute', 'demand', 'response'
Return=''
DATE=toDate(date)
Url=urlString(date,item)
try:
content=urllib2.urlopen(Url,timeout=default_timeout) # 超过响应时间则判Error
Return=content.read()
except:
print("Error..."+DATE)
pass
return Return
if __name__ == "__main__":
Item=['move']
default_timeout=60
for dx in range(6,5,-1):
for ix in Item:
content=get_page(dx,ix)
if (type(content)!=str or content==''):
print('------ cannot Catch '+str(dx)+'----')
break
origins=eval(content)
result=origins['result']
TrueDate=result['date']
TrueDate=TrueDate[0:4]+'-'+TrueDate[5:7]+'-'+TrueDate[8:10]
f=open(TrueDate+ix+'.csv','w')
mokyo=result['data']
for i in range(len(mokyo)):
print str(i)+'----'
line=mokyo[i]
for tis in range(len(line)):
arr=line[tis]
print len(arr[4])
f.write(str(i)+','+str(arr[1])+','+str(arr[2])+','+str(arr[3])+'\n')
f.close()
print(toDate(dx)+' finished...'+str(dx))
