'''Created on 30 05 2021@author: Enzo Cocca'''from builtins import objectclass FEATURES_LINE(object):    # def __init__"    def __init__(self,                 gid,                 location,                 name_f_l,                                  photo1,                 photo2,                 photo3,                 photo4,                 photo5,                 photo6,                                  the_geom                 ):        self.gid = gid  # 0        self.location = location # 1        self.name_f_l=name_f_l        self.photo1=photo1        self.photo2=photo2        self.photo3=photo3        self.photo4=photo4        self.photo5=photo5        self.photo6=photo6                self.the_geom = the_geom    # def __repr__"    def __repr__(self):        return "<FEATURES_LINE('%d','%s', '%s',%s,'%s','%s', '%s', '%s', '%s','%s')>" % (            self.gid,            self.location,            self.name_f_l,            self.photo1,            self.photo2,            self.photo3,            self.photo4,            self.photo5,            self.photo6,                        self.the_geom        )