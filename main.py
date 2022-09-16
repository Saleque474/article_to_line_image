from lines import lines

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image 
u=0
fonts=[
    "fonts/SutonnyOMJ.ttf"
]

for _font in fonts:

    with open("log.txt","r") as f:
        try:
            u=int(f.readlines()[0].replace("\n",""))
            print(u)
        except:
            u=0
        f.close()
    u+=1


    for _i,l in enumerate(lines):
        if len(l)<30:
            continue
        i=_i+u
        width=int(512*4)
        img = np.full((40,width,3),255, np.uint8)
        pil_im = Image.fromarray(img)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype(_font,size=40,)
        try:
            s=l.index(" ")
            e=l.index(" ",-15,-1)
            l=l[s+1:e]
            l=l.replace("  ","")
        except:
            continue
        l=l.strip()
        draw.text((0, 4), l, font=font, fill='black',align="center")
        cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        # Array
        black_point=np.array([0, 0, 0],np.uint8)
        rows=np.array(cv2_im_processed)
        last_black_point_index=0
        for row in rows:
            result = np.where(row == black_point)
            if len(result[0])>0:
                if last_black_point_index<result[0][-1]:
                    last_black_point_index=result[0][-1]
                
        img=rows[:, :last_black_point_index+1]
        pil_im = Image.fromarray(img)
        #Display the image
        # cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
        # cv2.imshow(f"img",cv2_im_processed)
        #Save image
        img_name=f"bangla_4-ground-truth/{i}.tif"
        pil_im.save(img_name,dpi=(300,300))
        # cv2.imwrite(img_name, cv2_im_processed)
        # Write text
        with open(f"bangla_4-ground-truth/{i}.gt.txt",'w') as file:
            file.write(l)
            file.close()
        with open("log.txt",'w') as log:
            log.write(f"{i}\n")
            log.close()
        # if i>50:
        #     break
        # cv2.waitKey(0)

    # for _i,l in enumerate(lines):
    #     i=_i+2
    #     with open(f"{i}.gt.txt",'w') as file:
    #         file.write(l)
    #         file.close()
    #     print(i,l)