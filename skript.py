# 6. zadanie: stvorce
# autor: Tomáš Kozák
# datum: 7.12.2018

class Stvorce:

    def __init__(self, n):
        self.n = n
        self.k = int(2**n) 
        self.zoz = []
        self.c1 = ['1','2',
                   '3','4']
        def matica(n,zoz,k=0):
            k += 1
            if k == n:
                return zoz 
            zoz1 = []
            zoz2 = []
            zoz3 = []
            zoz4 = []
            for i in range(len(zoz)):
                zoz1 += ['1'+zoz[i]]
                zoz2 += ['2'+zoz[i]]
                zoz3 += ['3'+zoz[i]]
                zoz4 += ['4'+zoz[i]]
            zoz.clear()
            for i in range(2**(k)):
                for j in range(2**(k)):
                    zoz += [zoz1[j+i*2**(k)]]
                for j in range(2**(k)):
                    zoz += [zoz2[j+i*2**(k)]]
            for i in range(2**(k)):
                for j in range(2**(k)):
                    zoz += [zoz3[j+i*2**(k)]]
                for j in range(2**(k)):
                    zoz += [zoz4[j+i*2**(k)]]
            return matica(n,zoz,k) 
        
        self.zoz = matica(self.n,self.c1)
        for i in range(len(self.zoz)):
            self.zoz[i] = '-'+self.zoz[i]
    
    def urob(self, index):
        self.w = index
        if self.w == '':
            for i in range(len(self.zoz)):
                if self.zoz[i][0] == '-':
                    self.zoz[i] = 'X'+self.zoz[i][1:]
                elif self.zoz[i][0] == 'X':
                    self.zoz[i] = '-'+self.zoz[i][1:]
            return
        self.t = int(index)
        self.q = len(index)
        for i in range(len(self.zoz)):
            if self.zoz[i][:self.q+1] == '-'+self.w:
                self.zoz[i] = 'X'+self.zoz[i][1:]
            elif self.zoz[i][:self.q+1] == 'X'+self.w:
                self.zoz[i] = '-'+self.zoz[i][1:]
                
                
    def vypis(self):
        self.s = 0
        for i in range(self.k):
            for j in range(self.k):
                print(self.zoz[self.s][:1],end = '')
                self.s += 1 
            print()


stv = Stvorce(2)
stv.urob('23')
stv.vypis()
stv.urob('2')
stv.urob('3')
stv.vypis()
            
