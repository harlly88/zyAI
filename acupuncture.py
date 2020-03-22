from datetime import datetime
'''
根据疾病情况得出穴位按摩处方

'''
import webbrowser


class Acupuncture(object):    
    
    shichen=['子','丑','寅','卯','辰','己','午','未','申','酉','戌','亥']
    jingmai=['足少阳胆经','足厥阴肝经','手太阴肺经','手阳明大肠经','足阳明胃经','足太阴脾经',
             '手少阴心经','手太阳小肠经','足太阳膀胱经','足少阴肾经','手厥阴心包经','手少阳三焦经']
    
    jingmai_xuewei={
        '足少阳胆经':('瞳子髎','听会','上关','颌厌','悬颅','悬厘','曲鬓','率谷','天冲','浮白',
         '头窍阴','完骨','本神','阳白','头临泣','目窗','正营','承灵','脑空','风池',
         '肩井','渊液','辄筋','日月','京门','带脉','五枢','维道','居髎','环跳',
         '风市','中渎','膝阳关','阳陵泉','阳交','外丘','光明','阳辅','悬钟',
         '丘墟','足临泣','地五会','侠溪','足窍阴'),
        
        '足厥阴肝经':('大敦','行间','太冲','中封','蠡沟','中都','膝关',' 曲泉',' 阴包','足五里','阴廉','急脉','章门','期门'),
        
        '手太阴肺经':('中府','云门','天府','侠白','尺泽','孔最','列缺','经渠','太渊','鱼际','少商'),
        
        '手阳明大肠经':('商阳','二间','三间','合谷','阳溪','偏历','温溜','下廉','上廉','手三里',
         '曲池','肘髎','手五里','臂臑','肩髃','巨骨','天鼎','扶突','口禾髎','迎香'),
        
        '足阳明胃经':('承泣','四白','巨髎','地仓','大迎','颊车','下关','头维','人迎','水突',
         '气舍','缺盆','气户','库房','屋翳','膺窗','乳中','乳根','不容','承满',
         '梁门','关门','太乙','滑肉门','天枢','外陵','大巨','水道','归来','气冲',
         '髀关','伏兔','阴市','梁丘','犊鼻','足三里','上巨虚','条口','下巨虚',
         '丰隆','解溪','冲阳','陷谷','内庭','厉兑'),
        
        '足太阴脾经':('隐白','大都','太白','公孙','商丘','三阴交','漏谷','地机','阴陵泉',
         '血海','箕门','冲门','府舍','腹结','大横','腹哀','食窦','天溪','胸乡','周荣','大包'),
        
       
        '手少阴心经':('极泉','青灵','少海','灵道','通里','阴郄','神门','少府','少冲'),
        
        '手太阳小肠经':(
            '少泽','前谷','后溪','腕骨','阳谷','养老','支正','小海','肩贞',
            '臑俞','天宗','秉风','曲垣','肩外俞','肩中俞','天窗','天容','颧髎','听宫'
        ),
        '足太阳膀胱经':(
            '睛明','攒竹','眉冲','曲差','五处','承光','通天','络却','玉枕',
            '天柱','大杼','风门','肺俞','厥阴俞','心俞','督俞','膈俞',
            '肝俞','胆俞','脾俞','胃俞','三焦俞','肾俞','气海俞','大肠俞',
            '关元俞','小肠俞','膀胱俞','中膂俞','白环俞','上髎','次髎',
            '中髎','下髎','会阳','承扶','殷门','浮郄','委阳','委中','附分',
            '魄户','膏肓','神堂','譩譆','膈关','魂门','阳纲','意舍','胃仓',
            '肓门','志室','胞肓','秩边','合阳','承筋','承山','飞扬','跗阳',
            '昆仑','仆参','申脉','金门','京骨','束骨','足通骨','至阴'
         ),
        
        '足少阴肾经':(
            '涌泉','然谷','太溪','大钟','水泉','照海','复溜','交信','筑宾',
            '阴谷','横骨','大赫','气穴','四满','中注','肓俞','商曲','石关',
            '阴都','通谷','幽门','步廊','神封','灵墟','神藏','彧中','俞府'
        ),
        
        '手厥阴心包经':(
            '天池','天泉','曲泽','郄门','间使','内关','大陵','劳宫','中冲'
        ),
        
        '手少阳三焦经':(
            '关冲','液门','中渚','阳池','外关','支沟','会宗','三阳络','四渎',
            '天井','清冷渊','消泺','臑会','肩髎','天髎','天牖','翳风','瘈脉',
            '颅息','角孙','耳门','耳和髎','丝竹空'
            )

        }
    
    '''十二井穴用于退热神昏热闭'''
    jinxue=('足窍阴','大敦','少商','商阳','历兑','隐白','少冲','少泽','至阴','涌泉','中冲','关冲')
    '''荥穴用于发烧'''
    yinxue=()
    '''郄穴用于疼痛'''
    xixue=()
    '''经穴'''
    jingxue=()
    '''合穴'''
    hexue=()
    '''原穴'''
    yuanxue=()
    '''俞穴'''
    shuxue=()
    '''募穴'''
    muxue=()
    
    '''
        疼痛部位
    '''
    tenTongBuWei={
        
        
    }
    '''
    经脉主病
    '''
    jingmai_bing={}
    
    '''到百度百科词条的链接
        比如穴位经脉
    '''
    
    def getBaiduLink(self,data):
        
        return ('https://baike.baidu.com/item/%s' % data)
    
    def getXueWeiLink(self,xuewei):
        return self.getBaiduLink(xuewei+'穴')
        
    
    def getCurrentCtime(self):
        '''
            计算当前天干地支
        
        '''
        current = datetime.now()
        hour = current.hour
        
        if hour <1 or hour>=23 :
            return self.shichen[0]
        elif hour >=1 and hour <3:
            return self.shichen[1]
        elif hour>=3 and hour<5:
            return self.shichen[2]
        elif hour>=5 and hour<7 :
            return self.shichen[3]
        elif hour>=7 and hour<9 :
            return self.shichen[4] 
        elif hour>=9 and hour<11 :
            return self.shichen[5]
        elif hour >=11 and hour <13:
            return self.shichen[6]
        elif hour>=13 and hour<15:
            return self.shichen[7]
        elif hour>=15 and hour<17:
            return self.shichen[8]
        elif hour>=17 and hour<19:
            return self.shichen[9]
        elif hour>=19 and hour<21:
            return self.shichen[10]
        else :
            return self.shichen[11]
         
    '''
        得出当前循行经脉
    '''    
    def getCurrentJinmai(self,sc):
        if not sc or self.shichen.index(sc)==-1:
            sc =self.getCurrentCtime()
        return self.jingmai[self.shichen.index(sc)]     
    
    '''得出当前循行经脉穴位的超文件链接'''
    def getCurrentJingMaiXueWeiLink(self):
        shiChen = self.getCurrentCtime()
        jingMai= self.getCurrentJinmai(shiChen)
        jinXue = self.jingmai_xuewei.get(jingMai)
        url ='<div>当前循行经脉为<a href="'+self.getBaiduLink(jingMai)+'" target="blank">'+jingMai+'</a></div><br>'
        for xuewei in jinXue:
            url = url+' &nbsp;&nbsp;&nbsp;<a href="'+self.getXueWeiLink(xuewei)+'" target="blank" >'+xuewei+'</a>'
            
        return url   
       
    '''
        得出灵龟八法子午流注开穴
    '''
    def getCurrentPoint(self):
        pass
    
    
    def diseaseRoad(self):
        pass
    
if __name__ =='__main__':
    ac = Acupuncture()
    print (ac.getCurrentJingMaiXueWeiLink())
    
    
