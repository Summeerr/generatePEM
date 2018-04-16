#coding=utf-8
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
os.system("cat push_key_dis.pem push_key_dis.pem > push_dis123.pem")
#是否需要验证，默认需要。
if val == 'true':
    #验证dev和dis证书有效性，一般不会出问题
    os.system('openssl s_client -connect gateway.sandbox.push.apple.com:2195 -cert push_developer_cer.pem -key push_key_cer.pem')
    os.system('openssl s_client -connect gateway.push.apple.com:2195 -cert push_dis_cer.pem -key push_key_dis.pem')
