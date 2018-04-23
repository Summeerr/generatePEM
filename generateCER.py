#coding=utf-8

#iOS快速生成推送的pem文件
#使用这个文件，我们需要制定一个规范，不然肯定是不成功的，我不是很喜欢制定规则的人，但是由于技术有限，所以必须这样
#1.我们最好先创建一个文件夹，为了便于管理证书。该文件夹下应该有生产的cer，p12和生产的cer，p12，总共四个证书。 
#2.格式需要如下python /Users/huxiang/Desktop/generateCER.py -dev=/Users/huxiang/Desktop/cer-p12/aps_development.cer,/Users/huxiang/Desktop/cer-p12/aps_development.p12 -dis=/Users/huxiang/Desktop/cer-p12/aps_distribution.cer,/Users/huxiang/Desktop/cer-p12/aps_distribution.p12 -val=true 
#3.注意像这个-dev=文件.p12,文件.cer这两个文件是没有先后顺序的，其次，如果你是先直接拖拽文件进去的时候，默认会在文件后面加空格，需要去掉空格。 
#4.字段说明:-dev后面是接的开发证书。-dis后面的是生产证书。-val后面意思是否验证证书，传入ture代表验证证书，默认不验证，一般不会出问题的。
import argparse
import os
import sys
def file_extension(path):
    return os.path.splitext(path)[1]

parser  = argparse.ArgumentParser(description='to create pem file')
parser.add_argument('-dev', type=str, default = None)
parser.add_argument('-dis', type=str, default = None)
parser.add_argument('-val', type=str ,default = 'false')
args   = parser.parse_args()
print args.dev
print args.dis
devArr = args.dev.split(',')
disArr = args.dis.split(',')
val    = args.val

#生成dev证书的pem文件
if(file_extension(devArr[0]) == '.cer'):
#    print ("openssl x509 -in "+ devArr[0]+"-inform der -out " + (devFilePath+'/push_developer_cer.pem'))
#    print ('openssl pkcs12 -nocerts -out ' + 'push_key_cer123.pem' +' -in '+devArr[1])
    os.system("openssl x509 -in "+ devArr[0]+" -inform der -out " + ('push_developer_cer.pem'))
    os.system('openssl pkcs12 -nocerts -out ' + 'push_key_cer.pem' +' -in '+devArr[1])
else:
    os.system("openssl x509 -in "+ devArr[1]+" -inform der -out " + ('push_developer_cer.pem'))
    os.system('openssl pkcs12 -nocerts -out ' + 'push_key_dev.pem' +' -in '+devArr[0])

os.system("cat push_developer_cer.pem push_key_cer.pem > push_dev123.pem")

#生成dis证书的pem文件
if(file_extension(disArr[0]) == '.cer'):
    os.system("openssl x509 -in "+ disArr[0]+" -inform der -out " + ('push_dis_cer.pem'))
    os.system('openssl pkcs12 -nocerts -out ' + 'push_key_dis.pem' +' -in '+disArr[1])
else:
    os.system("openssl x509 -in "+ disArr[1]+" -inform der -out " + ('push_dis_cer.pem'))
    os.system('openssl pkcs12 -nocerts -out ' + 'push_key_dis.pem' +' -in '+disArr[0])
os.system("cat push_dis_cer.pem push_key_dis.pem > push_dis123.pem")
#是否需要验证，默认需要。
if val == 'true':
    #验证dev和dis证书有效性，一般不会出问题
    os.system('openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert push_developer_cer.pem -key push_key_cer.pem')
    os.system('openssl s_client -connect gateway.push.apple.com:2195 -cert push_dis_cer.pem -key push_key_dis.pem')
