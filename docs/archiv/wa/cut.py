from rembg import remove,new_session
from PIL import Image,ImageFilter,ImageEnhance,ImageDraw
import sys
s=new_session('u2net')
items=[('02120','p01'),('02139','p02'),('02122','p03'),('02101','p04'),('02085','p05'),('02124','p06'),('02130','p07'),('02072','p08'),('02079','p09'),('02144','p10')]
W,H=1200,900
def bg():
    b=Image.new('RGB',(W,H));d=ImageDraw.Draw(b)
    for y in range(H):
        t=y/H; c=tuple(int(a+(bb-a)*t) for a,bb in zip((250,251,252),(222,227,233)))
        d.line([(0,y),(W,y)],fill=c)
    return b
for src,out in items:
    im=Image.open(f'dl/DSC{src}.jpg').convert('RGB')
    im=ImageEnhance.Color(im).enhance(1.15); im=ImageEnhance.Brightness(im).enhance(1.08); im=ImageEnhance.Contrast(im).enhance(1.08)
    o=remove(im,session=s); bb=o.getbbox(); o=o.crop(bb)
    sc=min(W*0.78/o.width,H*0.72/o.height); o=o.resize((int(o.width*sc),int(o.height*sc)),Image.LANCZOS)
    b=bg(); x=(W-o.width)//2; y=(H-o.height)//2-20
    sh=Image.new('RGBA',(W,H),(0,0,0,0)); ds=ImageDraw.Draw(sh)
    ds.ellipse([x+o.width*0.08,y+o.height-18,x+o.width*0.92,y+o.height+22],fill=(0,0,0,90)); sh=sh.filter(ImageFilter.GaussianBlur(18))
    b.paste(sh,(0,0),sh); b.paste(o,(x,y),o); b.save(f'cut/{out}.jpg',quality=88); print(out)
