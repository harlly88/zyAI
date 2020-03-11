from datetime import datetime
'''
根据疾病情况得出穴位按摩处方

'''


class Acupuncture(object):    
    
    shichen=('子','丑','寅','卯','辰','己','午','未','申','酉','戌','亥')
    jingmai=('胆','肝','肺','大肠','胃','脾','心','小肠','膀胱','肾','心包','三焦')
    '''十二井穴'''
    jinxue=()
    '''荥穴'''
    yinxue=()
    '''郄穴'''
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
    tentongbuwei={
        
        
        }
    
    
    def getCurrentCtime(self):
        '''
            计算当前天干地支
        
        '''
        current = datetime.now()
        hour = current.hour
        shichen = 0 
        if hour <1 or hour>=23 :
            return shichen[0]
        elif hour >=1 and hour <3:
            return shichen[1]
        elif hour>=3 and hour<5:
            return shichen[2]
        elif hour>=5 and hour<7 :
            return shichen[3]
        elif hour>=7 and hour<9 :
            return shichen[4] 
        elif hour>=9 and hour<11 :
            return shichen[5]
        elif hour >=11 and hour <13:
            return shichen[6]
        elif hour>=13 and hour<15:
            return shichen[7]
        elif hour>=15 and hour<17:
            return shichen[8]
        elif hour>=17 and hour<19:
            return shichen[9]
        elif hour>=19 and hour<21:
            return shichen[10]
        else :
            return shichen[11]
         
        
    def getCurrntJinmai(self,sc):
        if not shichen or shichen.index(sc)==-1:
            sc =self.getCurrentCtime()
        return self.shichen[shichen.index(sc)]        
       
    
    def getCurrentPoint(self):
        pass
    
    
    def diseaseRoad(self):
        pass
