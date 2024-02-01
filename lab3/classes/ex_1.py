class Upper_string:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'{self.name}'
    
p1 = Upper_string(input().upper())
print(p1)