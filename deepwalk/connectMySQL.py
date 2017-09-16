#coding=utf-8
import MySQLdb
import os
import traceback
from urllib import urlretrieve
from flowpic import image_flow
location= '/home/yao/Desktop/pythonsql/';


def connectAndtoFlow():
	conn = MySQLdb.connect(
		host='localhost',
		port=3306,
		user='root',
		passwd='123456',
		db='deepwalk'
		)
	cur = conn.cursor()
	sql = "select * From image; "
	#查询操作,返回地址的列表
	sqlUpdata ="update image set name=\"replacename\" where id = replaceid"


	try:
		#执行Sql语句
		cur.execute(sql)

		#print cur
		
		results = cur.fetchall()

		i = 0

		length = len(results)
		print results
		print length
		piclocation = '/home/yao/django_test/deepwalk/deepwalk/pic/'#picture address

		while  i < length -1  :
			if i == 0 :	
				urlretrieve(results[i][2] +'/'+ results[i][1] , piclocation + '/' + results[i][1])
				urlretrieve(results[i+1][2] +'/'+ results[i+1][1] , piclocation + '/' + results[i+1][1])
	
			else:
				urlretrieve(results[i+1][2] + '/' + results[i][1] , piclocation +'/'+ results[i][1])	
			print piclocation+'/' , piclocation.replace('pic' , 'flow') , results[i][1] , results[i+1][1]
			
			image_flow(piclocation+'/' , piclocation.replace('pic' , 'flow') , results[i][1] , results[i+1][1])
			#name = 'eating'
			name = 'eating'
#			updata = sqlUpdata.replace('replacename' , name).replace('replaceid' , str(results[i][0]))
			print 111
#			cur.execute(updata)
			i = i + 1 ;
			print i 

		for row in results:

			piclocation = location + str(i) + '.jpg'

			i = i + 1 	

	except Exception as e:
		print traceback.format_exc()
		print "Error:unable to fecth data"



	cur.close()
	conn.commit()

	conn.close()


if __name__ == "__main__":
	connectAndtoFlow()
	connectAndtoFlow()









	

