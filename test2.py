import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image 

string="""পেনে বসবাসরত পশ্চিমী রোমানদের উত্তরাধিকারী ভিজিগথ
শাসকদের মধ্যে উয়াম্বা এবং উইতিজা সুশাসন ও জনহিতকর কার্যের জন্য 
সুবিখ্যাত ও জনপ্রিয় ছিলেন। উয়াম্বার শাসনকালে স্পেন শান্তি শৃঙ্খলা ও 
সমৃদ্ধি লাভ করিলেও পরবর্তীকালে উয়াম্বা উচ্চাভিলাষী হইয়া উঠিলে 
অভিজাত সম্প্রদায় ও যাজকদের ষড়যন্ত্রের শিকারে পরিণত হয়। ফলে 
স্পেনে অনৈক্য ও বিশৃঙ্খলা দেখা দেয়। মুসা ইবনে নুসাইর১৬ যখন 
তিউনিসিয়ার ভাইসরয় ছিলেন সেই সময়ে বায়েটিকার ডিউক ৮২ বৎসর 
বয়স্ক রডারিক (লুজরিক) রাজা উইতিজাকে১৭ হত্যা করিয়া আইবেরিয়ার 
সিংহাসন অধিকার করেন। উইতিজা ৭০২ খ্রীস্টাব্দে তাঁহার পিতা এজিকার 
উত্তরাধিকারী নির্বাচিত হন এবং তিনি তাঁহার পুত্র আচিলাকে (আখিলা) 
৪১৪ খ্রীস্টাব্দের প্রারম্ভে ভিজিগথগণ কর্তৃক দখলকৃত উত্তর-পূর্ব স্পেনের 
রোমান প্রদেশ তারাকোনেন্সিস-এ গভর্নর নিযুক্ত করেন। আচিলা রডারিক 
কর্তৃক সিংহাসনচ্যুত হইয়া গ্যালিসিয়ায় পলায়ন করেন।
রাজতন্ত্র তাহার পূর্ব জৌলুস হারাইয়া ফেলে। সেনাবাহিনীর মধ্যে অসন্তুষ্টির 
"""

_font="fonts/SutonnyOMJ.ttf"
width=int(512*4)
img = np.full((400,width,3),255, np.uint8)
pil_im = Image.fromarray(img)
draw = ImageDraw.Draw(pil_im)
font = ImageFont.truetype(_font,size=40,)

l=string
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
img_name=f"generate_img/a.tif"
pil_im.save(img_name,dpi=(300,300))