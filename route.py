from directory import Directory
from render_figure import RenderFigure
from myscript import Myscript
from user import User
from myrecording import Myrecording
from place import Place
from person import Person
from country import Country
from event import Event
from periode import Periode
from stuff import Stuff
from group_stuff import Group_stuff
from hack import Hack
from gossip import Gossip


from mypic import Pic
from javascript import Js
from stylesheet import Css
import re
import traceback
import sys

class Route():
    def __init__(self):
        self.dbUsers=User()
        self.Program=Directory("premiere radio")
        self.Program.set_path("./")
        self.mysession={"notice":None,"email":None,"name":None}
        self.dbScript=Myscript()
        self.dbRecording=Myrecording()
        self.dbRumeur=Gossip()
        self.dbLieu=Place()
        self.dbStuff=Stuff()
        self.dbEvent=Event()
        self.dbGroupStuff=Group_stuff()
        self.dbPeriode=Periode()
        self.dbPersonne=Person()
        self.dbCountry=Country()
        self.dbHack=Hack()
        self.render_figure=RenderFigure(self.Program)
        self.getparams=("id",)
    def set_post_data(self,x):
        self.post_data=x
    def get_post_data(self):
        return self.post_data
    def set_my_session(self,x):
        print("set session",x)
        self.Program.set_my_session(x)
        self.render_figure.set_session(self.Program.get_session())
    def set_redirect(self,x):
        self.Program.set_redirect(x)
        self.render_figure.set_redirect(self.Program.get_redirect())
    def render_some_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_some_json(x)
    def render_my_json(self,x):
        self.Program.set_json(True)
        return self.render_figure.render_my_json(x)
    def set_json(self,x):
        self.Program.set_json(x)
        self.render_figure.set_json(self.Program.get_json())
    def set_notice(self,x):
        print("set session",x)
        self.Program.set_session_params({"notice":x})
        self.render_figure.set_session(self.Program.get_session())
    def set_session(self,x):
          print("set session",x)
          self.Program.set_session(x)
          self.render_figure.set_session(self.Program.get_session())
    def get_this_get_param(self,x,params):
          print("set session",x)
          hey={}
          for a in x:
              hey[a]=params[a][0]
          return hey
          
    def get_this_route_param(self,x,params):
          print("set session",x)
          return dict(zip(x,params["routeparams"]))
          
    def logout(self,search):
        self.Program.logout()
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def chat(self,search):
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/chat.html")
    def welcome(self,search):
        return self.render_figure.render_figure("welcome/index.html")
    def voirmoussaillon(self,params):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        personn1=self.dbPersonne.getbyid(myparam["id"])
        self.render_figure.set_param("user",personn1)
        return self.render_some_json("welcome/voirmoussaillon.json")
    def getmoussaillon(self,search):
        hi=self.dbPersonne.getall()
        self.render_figure.set_param("moussaillon",self.dbPersonne.getallbyname(search["id"][0]))
        return self.render_some_json("welcome/moussaillon.json")
    def audio_save(self,search):
        myparam=self.get_post_data()(params=("recording",))
        hi=self.dbRecording.create(myparam)
        return self.render_some_json("welcome/hey.json")
    def allscript(self,search):
        #myparam=self.get_post_data()(params=("name","content",))
        hi=self.dbScript.getall()
        self.render_figure.set_param("scripts",hi)
        return self.render_figure.render_figure("welcome/allscript.html")
    def lancerscript(self,search):
        myparam=search["myid"][0]
        hi=self.dbScript.getbyid(myparam)
        print(hi, "my script")
        a=self.scriptpython(hi["name"]).lancer()
        return self.render_some_json("welcome/monscript.json")


    def new1(self,search):
        myparam=self.get_post_data()(params=("script","missiontarget_id","missiontype_id","missionprogram_id",))
        #hi=self.dbMissionscript.create(myparam)
        return self.render_some_json("welcome/mypic.json")
    def nouveaulieu(self,search):
        myparam=self.get_post_data()(params=("pic","name",))
        self.render_figure.set_param("redirect","/")
        x=self.dbLieu.create(myparam)
        if x:
          self.set_notice("votre lieu a été ajouté")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouveauhack(self,search):
        myparam=self.get_post_data()(params=("person_id","place_id","text",))
        self.render_figure.set_param("redirect","/")
        x=self.dbHack.create(myparam)
        if x:
          self.set_notice("votre hack a été ajouté")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouvellerumeur(self,search):
        myparam=self.get_post_data()(params=("person_id","place_id","text",))
        self.render_figure.set_param("redirect","/")
        x=self.dbRumeur.create(myparam)
        if x:
          self.set_notice("votre rumeur a été ajoutée")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouvelleperiode(self,search):
        myparam=self.get_post_data()(params=("name",))
        self.render_figure.set_param("redirect","/")
        x=self.dbPeriode.create(myparam)
        if x:
          self.set_notice("votre periode a été ajoutée")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouvelevent(self,search):
        myparam=self.get_post_data()(params=("name","stuff_id","periode_id","person_ids"))
        self.render_figure.set_param("redirect","/")
        x=self.dbEvent.create(myparam)
        if x:
          self.set_notice("votre event a été ajoutée")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouveaustuff(self,search):
        myparam=self.get_post_data()(params=("name","group_stuff_id"))
        self.render_figure.set_param("redirect","/")
        x=self.dbStuff.create(myparam)
        if x:
          self.set_notice("votre stuff a été ajoutée")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouveaugroupstuff(self,search):
        myparam=self.get_post_data()(params=("name",))
        self.render_figure.set_param("redirect","/")
        x=self.dbGroupStuff.create(myparam)
        if x:
          self.set_notice("votre group stuf a été ajoutée")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def nouvellepersonne(self,search):
        myparam=self.get_post_data()(params=("name","pic","country_id"))
        self.render_figure.set_param("redirect","/")
        x=self.dbPersonne.create(myparam)
        if x:
          self.set_notice("votre personne a été ajoutée")
        else:
          self.set_code422(True)
        return self.render_some_json("welcome/redirect.json")
    def monscript(self,search):
        myparam=self.get_post_data()(params=("name","content",))
        hey=self.dbCommandline.create(myparam)
        hi=self.dbScript.create(myparam)
        print(hey,hi)
        return self.render_some_json("welcome/monscript.json")
    def enregistrer(self,search):
        print("hello action")
        self.render_figure.set_param("enregistrer",True)
        return self.render_figure.render_figure("welcome/radio.html")
    def hello(self,search):
        self.render_figure.set_param("users",self.dbPersonne.gettrois())
        print("hello action")
        return self.render_figure.render_figure("welcome/index.html")
    def delete_user(self,params={}):
        getparams=("id",)
        myparam=self.post_data(self.getparams)
        self.render_figure.set_param("user",User().deletebyid(myparam["id"]))
        self.set_redirect("/")
        return self.render_figure.render_redirect()
    def edit_user(self,params={}):
        getparams=("id",)

        myparam=self.get_this_route_param(getparams,params)
        print("route params")
        self.render_figure.set_param("user",User().getbyid(myparam["id"]))
        return self.render_figure.render_figure("user/edituser.html")
    def voirlieu(self,params={}):
        getparams=("id",)

        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)

        try:
          lieu1=self.dbLieu.getbyid(myparam["id"])
          self.render_figure.set_param("lieu",self.dbLieu.getbyid(myparam["id"]))
          if not lieu1:
            self.Program.set_code422(True);
            return self.render_some_json("ajouter/lieu1.json")
          return self.render_some_json("ajouter/lieu.json")
        except:
          self.Program.set_code422(True);
          return self.render_some_json("ajouter/lieu1.json")
    def voirevenement(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        personn1=self.dbEvent.getbyid(myparam["id"])
        self.render_figure.set_param("event",self.dbEvent.getbyid(myparam["id"]))
        return self.render_figure.render_figure("ajouter/voirevent.html")
    def voirpersonne(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        personn1=self.dbPersonne.getbyid(myparam["id"])
        self.render_figure.set_param("person",personn1)
        self.render_figure.set_param("event",self.dbEvent.getallbypersonid(personn1["id"]))
        return self.render_figure.render_figure("ajouter/voirpersonne.html")
    def seeuser(self,params={}):
        getparams=("id",)
        print("get param, action see my new",getparams)
        myparam=self.get_this_route_param(getparams,params)
        return self.render_figure.set_param("user",User().getbyid(myparam["id"]))
    def myusers(self,params={}):
        self.render_figure.set_param("users",User().getall())
        return self.render_figure.render_figure("user/users.html")
    def mypics(self,params={}):
        self.render_figure.set_param("pics",self.dbFish.getall())
        return self.render_figure.render_figure("fish/fishes.html")
    def update_user(self,params={}):
        myparam=self.post_data(self.getparams)
        self.user=self.dbUsers.update(params)
        self.set_session(self.user)
        self.set_redirect(("/seeuser/"+params["id"][0]))
    def login(self,s):
        search=self.get_post_data()(params=("email","password","password_security"))
        self.user=self.dbUsers.getbyemailpwsecurity(search["email"],search["password"],search["password_security"])
        print("user trouve", self.user)
        if self.user["email"] != "":
            print("redirect carte didentite")
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/cartedidentite\"}")
        else:
            self.set_json("{\"redirect\":\"/youbank\"}")
            print("session login",self.Program.get_session())
        return self.render_figure.render_json()
    def ajouterevent(self,search):

        self.render_figure.set_param("periode",self.dbPeriode.getall())
        self.render_figure.set_param("stuff",self.dbStuff.getall())
        return self.render_figure.render_figure("ajouter/event.html")
    def ajouterstuff(self,search):

        self.render_figure.set_param("group_stuff",self.dbGroupStuff.getall())
        return self.render_figure.render_figure("ajouter/stuff.html")
    def comptermoussaillons(self,search):
        self.render_figure.set_param("parpays",self.dbPersonne.getallparpays())
        self.render_figure.set_param("parjob",self.dbPersonne.getallparjob())
        return self.render_figure.render_figure("ajouter/comptermoussaillons.html")
    def ajoutergroupstuff(self,search):

        return self.render_figure.render_figure("ajouter/group_stuff.html")
    def ajouterperiode(self,search):

        return self.render_figure.render_figure("ajouter/periode.html")
    def ajouterpersonne(self,search):

        self.render_figure.set_param("pays",self.dbCountry.getall())
        return self.render_figure.render_figure("ajouter/personne.html")
    def ajouterlieu(self,search):
        return self.render_figure.render_only_figure("ajouter/lieu.html")
    def ajouterhack(self,search):
        self.render_figure.set_param("personnes",self.dbPersonne.getall())
        self.render_figure.set_param("lieux",self.dbLieu.getall())
        return self.render_figure.render_only_figure("ajouter/hack.html")
    def ajouterrumeur(self,search):
        self.render_figure.set_param("personnes",self.dbPersonne.getall())
        self.render_figure.set_param("lieux",self.dbLieu.getall())
        return self.render_figure.render_only_figure("ajouter/rumeur.html")
    def nouveau(self,search):
        return self.render_figure.render_figure("welcome/new.html")
    def getlyrics(self,params={}):
        getparams=("id",)

       
        myparam=self.get_this_get_param(getparams,params)
        print("my param :",myparam)
        try:
          print("hey",hey)
          if not hey:
            hey=[]
        except:
          hey=[]

        self.render_figure.set_param("lyrics",hey)
        return self.render_some_json("welcome/lyrics.json")
    def jouerjeux(self,search):
        return self.render_figure.render_figure("welcome/jeu.html")

    def signin(self,search):
        return self.render_figure.render_figure("user/signin.html")

    def save_user(self,params={}):
        myparam=self.get_post_data()(params=("email","password","password_security","nomcomplet"))
        self.user=self.dbUsers.create(myparam)
        if self.user["user_id"]:
            self.set_session(self.user)
            self.set_json("{\"redirect\":\"/youbank\"}")
            return self.render_figure.render_json()
        else:
            self.set_json("{\"redirect\":\"/youbank_inscription\"}")
            return self.render_figure.render_json()
    def joueraujeu(self,params={}):
        self.set_json("{\"redirect\":\"/signin\"}")
        getparams=("song_id","jeu_id")
        myparam=self.get_post_data()(params=getparams)
        self.set_session_params(myparam)
        #self.set_redirect("/signin")
        #return self.render_figure.render_redirect()
        return self.render_figure.render_my_json("{\"redirect\":\"/signin\"}")
    def run(self,redirect=False,redirect_path=False,path=False,session=False,params={},url=False,post_data=False):
        if post_data:
            print("post data")
            self.set_post_data(post_data)
            print("post data set",post_data)
        if url:
            print("url : ",url)
            self.Program.set_url(url)
        self.set_my_session(session)

        if redirect:
            self.redirect=redirect
        if redirect_path:
            self.redirect_path=redirect
        if not self.render_figure.partie_de_mes_mots(balise="section",text=self.Program.get_title()):
            self.render_figure.ajouter_a_mes_mots(balise="section",text=self.Program.get_title())
        if path and path.endswith("png"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpeg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("gif"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("svg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith("jpg"):
            self.Program=Pic(path)
            self.Program.set_path("./")
        elif path and path.endswith(".jfif"):
            self.Program=Pic(path)
        elif path and path.endswith(".css"):
            self.Program=Css(path)
        elif path and path.endswith(".js"):
            self.Program=Js(path)
        elif path:
            path=path.split("?")[0]
            print("link route ",path)
            ROUTES={
            "^/moussaillon/([0-9]+).json$":self.voirmoussaillon,
            "^/event/([0-9]+)$":self.voirevenement,
            "^/personne/([0-9]+)$":self.voirpersonne,
            "^/lieu/([0-9]+)$":self.voirlieu,
            '^/nouvelevent$': self.nouvelevent,
            '^/comptermoussaillons$': self.comptermoussaillons,
            '^/ajouterevent$': self.ajouterevent,
            '^/nouveaustuff$': self.nouveaustuff,
            '^/ajouterstuff$': self.ajouterstuff,
            '^/nouveaugroupstuff$': self.nouveaugroupstuff,
            '^/ajoutergroupstuff$': self.ajoutergroupstuff,

            '^/getmoussaillon$': self.getmoussaillon,
            '^/nouvelleperiode$': self.nouvelleperiode,
            '^/ajouterperiode$': self.ajouterperiode,
            '^/nouvellepersonne$': self.nouvellepersonne,
            '^/ajouterpersonne$': self.ajouterpersonne,
            '^/new$': self.nouveau,
            '^/welcome$': self.welcome,
            '^/signin$': self.signin,
            '^/logmeout$':self.logout,
            '^/save_user$':self.save_user,
            '^/update_user$':self.update_user,
            "^/seeuser/([0-9]+)$":self.seeuser,
            "^/edituser/([0-9]+)$":self.edit_user,
            "^/deleteuser/([0-9]+)$":self.delete_user,
            '^/login$':self.login,

                                                                                                    '^/users$':self.myusers,
                    '^/$': self.hello

                    }
            REDIRECT={"/save_user": "/welcome"}
            for route in ROUTES:
               print("pattern=",route)
               mycase=ROUTES[route]
               x=(re.match(route,path))
               print(True if x else False)
               #code bon pour les erreurs dans le code python
               if x:
                   params["routeparams"]=x.groups()
                   try:
                       html=mycase(params)
                   except Exception as e:
                       print("erreur"+str(e),traceback.format_exc())
                       html=("<p>une erreur s'est produite dans le code server  "+(traceback.format_exc())+"</p><a href=\"/\">retour à l'accueil</a>").encode("utf-8")
                       print(html)
                   self.Program.set_html(html=html)
                   self.Program.clear_notice()
                   self.Program.redirect_if_not_logged_in()
                   return self.Program
               else:
                   self.Program.set_html(html="<p>la page n'a pas été trouvée</p><a href=\"/\">retour à l'accueil</a>")

        return self.Program
