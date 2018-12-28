import MySQLdb

def pass_check(id, passcode):
	presql = SELECT * FROM passcode WHERE id = '%s'"
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

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

print("please scan barcode or manually insert code followed by enter")
barcode = input()
please enter passcode
passcode = input()
check = pass_check(id = barcode, passcode = passcode)
	if check == "true"
		print("code recognised")
	else
		print("code not recognised")
		# need to return to start, this section will become yet another function
