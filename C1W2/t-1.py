import os
import tempfile
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--key",type=str)
parser.add_argument("--val",type =str)
parser.parse_args()
args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.key != None and args.val != None : 
    if os.path.exists(storage_path) is True :
    
        nev = {}
        new_nev = {}
    
        with open(storage_path,'r+') as inp:
        
            for i in inp.readlines():            
                key,val = i.strip().split(':')
                nev.update({key:val})
 
        for x in nev.keys():
            if x == args.key:
                val = nev.setdefault(args.key)
                val = val.split(', ')
                val.append(args.val)
                val = ', '.join(val)
                new_nev.update({args.key:val})
            else:
                new_nev.update(nev)
                new_nev.update({args.key:args.val})
            
    
        with open(storage_path,'w') as i:
            for key,val in new_nev.items():
                i.write('{}:{}\n'.format(key,val))          
    else: 
        nev = {}
        nev[args.key]= args.val
        with open(storage_path,'w') as i:
            for key,val in nev.items():
                i.write('{}:{}\n'.format(key,val))   
if args.key != None  and  args.val == None: 
    if os.path.exists(storage_path) is True :
        nev = {}  
        with open(storage_path,'r+') as inp:
            for i in inp.readlines():            
                key,val = i.strip().split(':')
                nev.update({key:val})
        value  = nev.setdefault(args.key)
        print(value) 
    else: 
        print("")           
