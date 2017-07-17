# -*- coding: utf-8 -*-
# @Author: Boya Chiou
# @Date:   2017-06-13 09:32:35
# @Last Modified by:   Boya Chiou
# @Last Modified time: 2017-07-17 19:46:24

import cx_Oracle
import sys
import time


class ORCL_CONN(object):
	"""docstring for SchemaTool"""
	def __init__(self):
		pass

	def CONN(self):
		dsnStr = cx_Oracle.makedsn("[your server IP]", "[your port]", "[your service name]")
		self.conn = cx_Oracle.connect(user="[user name]", password="[password]", dsn=dsnStr)
		
		self.c = self.conn.cursor()
		return self.c


	def Query(self, TableName):
		self.TableName = TableName
		sql = """SELECT * FROM {0} WHERE ROWNUM <= 1""".format(self.TableName)
		data = self.c.execute(sql)
		# for i in data:
		#	print i


	def SchemaInfo(self):
		# FOR MY OWN REFERENCE
		SchemaInfo = self.c.description
		for i in SchemaInfo:
			print i


	def SchemaExpo(self):
		HeaderInfo = self.c.description
		breaker = "/*-------------------------------BREAK LINE------------------------------------*/"

		with open("{0}.txt".format(self.TableName), 'w') as f:
			f.write('name, type, display_size, internal_szie, precision, scale, null_ok\n\n')

			f.write("CREATE TABLE {0}\n".format(self.TableName))
			f.write("(\n")
			for i in HeaderInfo:
				Name = '{0} '.format(str(i[0]))
				DataType = '{0} '.format(str(i[1]).rsplit('.',1)[1][:-2])
				Display_Size = '{0}'.format(str(i[2]))
				Precision = '{0}'.format(str(i[4]))
				
				f.write(Name)
		
				if DataType.strip() == "STRING":
					f.write("VARCHAR ")
					f.write("({0}),\n".format(Display_Size))
				elif DataType.strip() == "FIXED_CHAR": 
					f.write("CHAR ")
					f.write("({0}),\n".format(Display_Size))				
				elif DataType.strip() == "NUMBER":
					f.write("NUMERIC ")
					f.write("({0}),\n".format(Precision))
				elif DataType.strip() == "DATETIME":
					f.write("DATETIME,\n")
				else:
					f.write("None String/Numeric type not difined")
				# f.write('{0}\n'.format(str(i)))
			# f.write(breaker)
			f.write(")")


	def Big_Query(self):
		sql = """

		<please put your query here>

    		  """
		


		data = self.c.execute(sql)
		for i, e in enumerate(data):
			print "RECORD #{0}".format(i+1),'\n',e,'\n'


if __name__ == "__main__":
	S = ORCL_CONN()
	S.CONN()
	# table_name = raw_input("Please Enter Table Schema You'd Want to Export (e.g.: SCHEMA_NAME.TABLE_NAME): ")
	# S.Query(table_name)

	# Enter the table name of the table you'd like to download
	#S.Query("TABLE_NAME")
	#S.SchemaExpo()

	t0 = time.clock()
	# S.SchemaInfo()
	S.Big_Query()

	t1 = time.clock()

	print "Process Time: {0}".format(t1-t0)

	# Close Connection
	S.conn.close()
