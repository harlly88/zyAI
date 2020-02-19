# coding=utf-8
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

import streamlit as st
import numpy as np
import pandas as pd

st.title("呼吸道感染中医AI问诊V0.21")
a=5.0  #太阳症
b=5.0  #少阳证
c=5.0  #阳明证
d=5	 #湿
e=5  #头
f=5  #肺
g=5	 #胸
h=5  #上腹
i=5  #下腹
j=5  #膀胱
cout=1


st.sidebar.title('症状描述，有异常的症状按实际勾选')
if st.sidebar.checkbox('高烧>39'):
	a=a+8
	b=b+5
	c=c+6
	cout=cout+1
	e=e+5
elif st.sidebar.checkbox('低烧<39'):
	a=a+7
	b=b+8
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('无汗'):
	a=a+9
	b=b+5
	c=c+5
	cout=cout+1
	d=d+5
if st.sidebar.checkbox('干咳无痰'):
	a=a+5
	b=b+9
	c=c+5
	cout=cout+1
elif st.sidebar.checkbox('咳嗽白痰'):
	a=a+7
	b=b+5
	c=c+5
	cout=cout+1
	d=d+5
	f=f+5
elif st.sidebar.checkbox('咳嗽黄痰'):
	a=a+6
	b=b+7
	c=c+5
	cout=cout+1
	f=f+5
if st.sidebar.checkbox('舌苔白腻'):
	a=a+7
	b=b+5
	c=c+5
	cout=cout+1
	d=d+5
elif st.sidebar.checkbox('舌苔黄腻'):
	a=a+6
	b=b+5
	c=c+7
	cout=cout+1
if st.sidebar.checkbox('舌尖红'):
	a=a+5
	b=b+5
	c=c+7
	cout=cout+1
if st.sidebar.checkbox('舌边齿痕'):
	d=(d+5)
if st.sidebar.checkbox('头晕'):
	a=a+5
	b=b+9
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('鼻塞'):
	a=a+7
	b=b+5
	c=c+7
	cout=cout+1	
	e=e+5
if st.sidebar.checkbox('流清涕'):
	a=a+8
	b=b+5
	c=c+5
	cout=cout+1
	e=e+5
elif st.sidebar.checkbox('流黄涕'):
	a=a+6
	b=b+5
	c=c+7
	cout=cout+1
	e=e+5
if st.sidebar.checkbox('头顶或后部疼痛'):
	a=a+8
	b=b+5
	c=c+5
	cout=cout+1
	e=e+5
if st.sidebar.checkbox('额头附近疼痛'):
	a=a+7
	b=b+5
	c=c+8
	cout=cout+1
	e=e+5
if st.sidebar.checkbox('太阳穴附近疼痛'):
	a=a+5
	b=b+9
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('耳朵痛或耳鸣'):
	a=a+5
	b=b+9
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('眼睛痛，眼屎多或眼白发红'):
	a=a+5
	b=b+9
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('咽喉肿痛'):
	a=a+6
	b=b+5
	c=c+6
	cout=cout+1
	e=e+5
if st.sidebar.checkbox('捏后脖子痛'):
	a=a+7
	b=b+5
	c=c+5
	cout=cout+1
	e=e+5
	f=f+5
if st.sidebar.checkbox('揉咽喉下痛'):
	a=a+5
	b=b+7
	c=c+5
	cout=cout+1
	e=e+5
	f=f+5
if st.sidebar.checkbox('揉胸口痛'):
	a=a+5
	b=b+5
	c=c+7
	cout=cout+1
	g=g+5
if st.sidebar.checkbox('揉腋下痛'):
	a=a+5
	b=b+7
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('大便稀软或腹泻'):
	a=a+6
	b=b+6
	c=c+5
	cout=cout+1
	d=d+5
	h=h+5
if st.sidebar.checkbox('大便硬或便秘2天以上'):
	a=a+6
	b=b+6
	c=c+9
	cout=cout+1	
	i=i+5
if st.sidebar.checkbox('不爱喝水'):
	a=a+8
	b=b+5
	c=c+5
	cout=cout+1
	d=d+5
elif st.sidebar.checkbox('爱喝水'):
	a=a+5
	b=b+5
	c=c+8
	cout=cout+1	
	d=d-5
	h=h+5
if st.sidebar.checkbox('喜热水'):
	a=a+6
	b=b+5
	c=c+5
	cout=cout+1
elif st.sidebar.checkbox('喜凉水'):
	a=a+5
	b=b+5
	c=c+7
	cout=cout+1
	h=h+5
if st.sidebar.checkbox('呕吐或欲呕'):
	a=a+5
	b=b+8
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('尿偏黄'):
	a=a+5
	b=b+5
	c=c+7
	cout=cout+1
	i=i+5
elif st.sidebar.checkbox('尿偏白'):
	a=a+7
	b=b+5
	c=c+5
	cout=cout+1
	j=j+5
	d=d+5
if st.sidebar.checkbox('尿疼痛'):
	a=a+6
	b=b+5
	c=c+5
	cout=cout+1
	j=j+5
if st.sidebar.checkbox('关节酸痛'):
	a=a+7
	b=b+5
	c=c+5
	cout=cout+1
	j=j+5
if st.sidebar.checkbox('身体怕冷'):
	a=a+8
	b=b+5
	c=c+5
	cout=cout+1
if st.sidebar.checkbox('身体乏力'):
	a=a+5
	b=b+5
	c=c+5
	cout=cout+1
	g=g+5
	d=d+5



a=a/cout
b=b/cout
c=c/cout
if a==max(a,b,c) and a>6 :
	st.write('主症为伤寒太阳症，足太阳膀胱经受邪，身体有寒，建议后脖子，后背刮痧，用生姜水擦后背。喝生姜红糖水，热稀饭，风寒感冒颗粒。盖厚被子，热水泡脚，让身体出些汗。')
	if a==b or a==c :
		a=a+1
if b==max(a,b,c) and b>6 :
	st.write('主症为伤寒少阳症，足少阳胆经受邪，建议腋下刮痧，喝小柴胡颗粒，卧床休息')
	if a==b or b==c :
		b=b+1
if c==max(a,b,c) and c>6 :
	st.write('主症为伤寒阳明症，足阳明胃经受邪，身体有热，建议前胸刮痧，揉腹，麻仁丸，通便')
	if a==c or b==c :
		c=c+1
num_list = [a,b,c,]
tmp_list = sorted(num_list)
if a==tmp_list[-2] and a>6 : 
	st.write('兼症为伤寒太阳症，足太阳膀胱经受邪，身体有寒，建议后脖子，后背刮痧，用生姜水擦后背。喝生姜红糖水，热稀饭，风寒感冒颗粒。盖厚被子，热水泡脚，让身体出些汗。')
if b==tmp_list[-2] and b>6 :
	st.write('兼症为伤寒少阳症，足少阳胆经受邪，建议腋下刮痧，喝小柴胡颗粒，卧床休息')
if c==tmp_list[-2] and c>6 :
	st.write('兼症为伤寒阳明症，足阳明胃经受邪，身体有热，建议前胸刮痧，揉腹，麻仁丸，通便')

if d>5 :
	st.write('身体有湿邪')
mingxi = []
if  e>5 :
	mingxi.extend(['头'])
if  f>5 :
	mingxi.extend(['肺'])
if  g>5 :
	mingxi.extend(['胸'])
if  h>5 :
	mingxi.extend(['上腹'])
if  i>5 :
	mingxi.extend(['下腹'])
if  j>5 :
	mingxi.extend(['膀胱'])
abc = [str(i) for i in mingxi]
xyz = " "
st.write('病邪淤堵部位主要为:' ,xyz.join(abc))

#桂枝,白芍,炙甘草,大枣,生姜,麻黄,杏仁,葛根,柴胡,黄芩,枳实,厚朴,大黄,'白芍','炙甘草','大枣','生姜'
yaofang = []
if a==max(a,b,c) and a>6 :  #太阳症
	yaofang.extend(["桂枝",'白芍','炙甘草','大枣','生姜'])
if b==max(a,b,c) and b>6 :  #少阳证
	yaofang.extend(['柴胡','黄芩','法半夏','党参','大枣','炙甘草'])
if c==max(a,b,c) and c>6 :  #阳明证
	yaofang.extend(['枳实','厚朴','大黄'])
if a==tmp_list[-2] and a>6 : 
	yaofang.extend(['桂枝','白芍','炙甘草','大枣','生姜'])
if b==tmp_list[-2] and b>6 :
	yaofang.extend(['柴胡','黄芩','法半夏','党参','大枣','炙甘草'])
if c==tmp_list[-2] and c>6 :
	yaofang.extend(['枳实','厚朴','大黄'])
if d>5 :  #湿
	yaofang.extend(['茯苓',])
	if f>5 :
		yaofang.extend(['陈皮'])
	if g>5 :
		yaofang.extend(['瓜蒌'])
if e>5 :  #头
	yaofang.extend(['葛根'])
if f>5 :
	yaofang.extend(['麻黄','杏仁'])
if g>5 :
	yaofang.extend(['淡竹叶'])
if h>5 :
	yaofang.extend(['法半夏','生石膏'])
if i>5 :
	yaofang.extend(['大黄'])
if j>5 :
	yaofang.extend(['泽泻'])
news_ids = []
for id in yaofang:
    if id not in news_ids:
        news_ids.append(id)
result = [str(i) for i in news_ids]
str = " "
st.write('建议中药:',str.join(result))
