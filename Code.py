n="samsung,'OEM Samsung Washing Machine Pulsator Washplate Cap Shipped With WA48J7700AW, WA48J7700AW/A2, WA48J7700AW/AA',20916,samsung,'OEM Samsung Chrome Washing Machine Washplate Pulsator Cap Shipped With WA52M7750AV,WA52M7750AV/A4, WA52M7750AW, WA52M7750AW/A4',91995,samsung, 'SAMSUNG Washing Machine Spring Hanger, DC61-01257M', 22970,samsung,'Samsung DC97-17022BAssy Detergent',32959,samsung,'Samsung DC66-00470A DAMPERSHOCK',29981,samsung,'DC64-00519D Samsung Washing Machine Door Lock Washer Dryer Dishwashe -M #GH4498 349Y49HBRG9109150',52000,samsung,'Samsung DC97-16991A Assembly Filter',13000"
dict={}
key=""
val=0
for i in n.split(','):
    if i.isdigit()==True:
        val=i
        dict[key]=val
        key=""
        val=0
    else:
        key=key+i+','
for k,v in sorted(dict.items(),key=lambda item: item[1]):
    print(k,v)
