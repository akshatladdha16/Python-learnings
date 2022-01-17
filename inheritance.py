from chef import chef
from chinesechef import chinesechef
mychef=chef()
mychinesechef=chinesechef()
mychef.make_chicken()
mychinesechef.make_fried_rice()
mychinesechef.make_chicken()#here we overwrite make-chicken attribute in chinese chef class
mychinesechef.make_soup()#so here we can use chef attribute in chinese chef class
