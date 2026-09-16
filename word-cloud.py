import jieba
from matplotlib import pylab as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
from pymysql import *
import json

def get_img(field,targetImageSrc,resImageSrc):
    con = connect(host='localhost',user='root',password='root',database='cardata',port=3306,charset='utf8mb4')
    cusor = con.cursor()
    sql = f"select {field} from carinfo"
    cusor.execute(sql)
    data = cusor.fetchall()

    text = ''
    for i in data:
        if i[0] != '':
            tagArr = i
            for j in tagArr:
                text += j
    cusor.close()
    con.close()
    data_cut = jieba.cut(text,cut_all=False)
    string = ' '.join(data_cut)

    #图片
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        font_path='STHUPO.TTF',
        mask=img_arr,
        background_color= '#04122c'
    )
    wc.generate_from_text(string)
    #绘制图片
    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(resImageSrc,dpi=800,bbox_inches='tight',pad_inches=-0.1)


get_img('manufacturer','./big-screen-vue-datav-master/public/carCloud.png','./big-screen-vue-datav-master/public/car_cloud.png')

