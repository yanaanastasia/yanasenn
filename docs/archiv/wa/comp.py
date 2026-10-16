from PIL import Image,ImageFilter,ImageDraw
W,H=1200,900
def bg():
    b=Image.new('RGB',(W,H));d=ImageDraw.Draw(b)
    for y in range(H):
        t=y/H; d.line([(0,y),(W,y)],fill=tuple(int(a+(bb-a)*t) for a,bb in zip((250,251,252),(222,227,233))))
    return b
def comp(o,out,f):
    o=o.crop(o.getbbox()); sc=min(W*f/o.width,H*f/o.height); o=o.resize((int(o.width*sc),int(o.height*sc)),Image.LANCZOS)
    b=bg(); x=(W-o.width)//2; y=(H-o.height)//2-20
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(sh).ellipse([x+o.width*0.12,y+o.height-16,x+o.width*0.88,y+o.height+20],fill=(0,0,0,95)); sh=sh.filter(ImageFilter.GaussianBlur(18))
    b.paste(sh,(0,0),sh); b.paste(o,(x,y),o); b.save(out,quality=88)
comp(Image.open('ballcut2.png').convert('RGBA'),'cut/ball.jpg',0.72)
from rembg import remove,new_session
from PIL import ImageEnhance
im=Image.open('dl/DSC02079.jpg').convert('RGB'); im=ImageEnhance.Brightness(im).enhance(1.08)
comp(remove(im,session=new_session('u2net')),'cut/p09.jpg',0.38)
