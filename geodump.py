import mysql.connector
import json
import codecs

conn = mysql.connector.connect(
    host="b5yzxnyytnlxqdoxhyos-mysql.services.clever-cloud.com",
    user="uxqnmc8ewezthc0l",
    passwd="lnevNlwTCdDEIp2kMpNa",
    database="b5yzxnyytnlxqdoxhyos"
)
cur = conn.cursor()

#selects data from database
cur.execute('SELECT * FROM Locations')
#opens javascript list for data to go in
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1])
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue
    #formats fetched data in a format that can be visualised
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        #writes data into javascript list
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

