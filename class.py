class aayush:
    nam="STAR"
    planet="earth"
    def info(self):
     print(self.nam ,self.planet)
a=aayush()
a.nam="unokown"
print(f"{a.nam} is not a {a.planet}")    
a.info()