import MySQLdb

def pass_check(barcode, passcode):
	presql = "SELECT * FROM users WHERE barcode = '%s'"
	sql = presql % barcode
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        barcodetemp = row[0]
        passcodetemp = row[1]
	if passcode != passcodetemp:
    		print("wrongcode")
    		return false
	return true

def priv_check(barcode):
	presql = "SELECT * FROM users WHERE barcode = '%s'"
	sql = presql % barcode
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        role = row[5]
	if role == 1:
		return normal
	elif role == 2:
		return operator
	elif role == 3:
		return admin
	elif: role == 0:
		return prob
	else:
		print("a unexpected error occured, please contact a operator")
		return error
	
# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

print("please scan barcode or manually insert code followed by enter")
barcode = input()
please enter passcode
passcode = input()
check = pass_check(barcode = barcode, passcode = passcode)
	if check == "true"
		print("code recognised")
	else
		print("code not recognised")
		# need to return to start, this section will become yet another function
print("
