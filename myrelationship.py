# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Myrelationship(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists myrelationship(
        id integer primary key autoincrement,
        relation1_id text,
            relation2_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select myrel.*,r2.name as relation2, r1.name as relation1 from myrelationship myrel left join relationship r1 on r1.id = myrel.relation1_id left join relationship r2 on r2.id = myrel.relation2_id")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from myrelationship where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from myrelationship where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into myrelationship (relation1_id,relation2_id) values (:relation1_id,:relation2_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["myrelationship_id"]=myid
        azerty["notice"]="votre myrelationship a été ajouté"
        return azerty




