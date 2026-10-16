from rembg import remove,new_session
from PIL import Image,ImageFilter
s=new_session('u2net')
M=[('02120','p01'),('02139','p02'),('02122','p03'),('02143','ball'),('02101','p04'),('02085','p05'),('02124','p06'),('02130','p07'),('02072','p08'),('02079','p09')]
for src,out in M:
    im=Image.open(f'orig/{src}.jpg').convert('RGB'); sm=im.resize((1500,1000))
    x0,y0,x1,y1=remove(sm,session=s,only_mask=True).point(lambda v:255 if v>128 else 0).getbbox()
    k=4; x0,y0,x1,y1=x0*k,y0*k,x1*k,y1*k
    w,h=x1-x0,y1-y0; cx,cy=(x0+x1)/2,(y0+y1)/2
    W=max(w*1.45,h*1.45*4/3,1600); H=W*3/4
    W=min(W,6000);H=min(H,4000);W=H*4/3
    l=max(0,min(6000-W,cx-W/2)); t=max(0,min(4000-H,cy-H/2))
    c=im.crop((int(l),int(t),int(l+W),int(t+H))).resize((1600,1200),Image.LANCZOS).filter(ImageFilter.UnsharpMask(1,40,2))
    c.save(f'page/img/{out}.jpg',quality=88); print(out,int(W))
