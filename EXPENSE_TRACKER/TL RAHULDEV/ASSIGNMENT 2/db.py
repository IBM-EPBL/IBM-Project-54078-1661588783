prerequisite:
  i.  Install packages python3; 
 ii.  python3-pip;
iii.  python3-ibm_db;
 iv.  python3-itoolkit
 
 Install the PrettyTable python library:
 " $ pip3 install PTable "
 
 Create "kpretty.py" and type the below code:
 
 " from prettytable import from_db_cursor
  import ibm_db_dbi as db2
  conn = db2.connect()
  cur = conn.cursor()
  cur.execute("select * from qiws.qcustcdt")
      print(from_db_cursor(cur)) "
      
Now run the code:
 $ python3 kpretty.py