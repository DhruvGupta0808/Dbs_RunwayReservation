CREATE TABLE airplane_schedule(plane_id VARCHAR(5) PRIMARY KEY, arrival_time FLOAT(4,2) , departure_time FLOAT(4,2) )

CREATE TABLE new_airplane_entries(plane_id VARCHAR(5) PRIMARY KEY, arrival_time FLOAT(4,2) , departure_time FLOAT(4,2) )

CREATE TABLE rejected_airplane_entries(plane_id VARCHAR(5) PRIMARY KEY, arrival_time FLOAT(4,2) , departure_time FLOAT(4,2) )

INSERT INTO new_airplane_entries VALUES(%s,%s,%s)",(p_id,a_time,d_time)

INSERT INTO rejected_airplane_entries SELECT %s,%s,%s from dual WHERE EXISTS (SELECT * FROM airplane_schedule WHERE ABS((FLOOR(%s)*60 + (%s-FLOOR(%s))*100.00)-(FLOOR(arrival_time)*60 + (arrival_time-FLOOR(arrival_time))*100.00))<5)",(p_id,a_time,d_time,a_time,a_time,a_time)

INSERT INTO airplane_schedule SELECT %s,%s,%s from dual WHERE NOT EXISTS (SELECT * FROM airplane_schedule WHERE ABS((FLOOR(%s)*60 + (%s-FLOOR(%s))*100.00)-(FLOOR(arrival_time)*60 + (arrival_time-FLOOR(arrival_time))*100.00))<5)",(p_id,a_time,d_time,a_time,a_time,a_time)

SELECT * FROM airplane_schedule

SELECT * FROM rejected_airplane_entries

SELECT * FROM new_airplane_entries