# args 
def full_name(first, last, *args):
    print(first,last)
    name = f'{first} {last}' # fstring
    print(name)
    print(args)
    for name in args:
        print('name sent in args: ',name)

full_name('hasan', 'semon' , 'montu', 'emon')

#kargs

def full_name(first, last, **kargs): #kargs means arguments with keys 
    # print(first, last) 
    print(f'{first} {last}')

    print(kargs)
    print(kargs['title']) #print with keys

    for key,value in kargs.items():
        print(key,value)

full_name(first ='mohiminul',last = 'islam',title ='semon',title2 ='eram',title3 ='abdullah')