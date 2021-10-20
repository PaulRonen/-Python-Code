import file_functtion as ff

data = ff.reader('radiants.txt')
print(len(data),'chars is file')

data = ff.reader('dummy.txt')
print(len(data),'chars is file')