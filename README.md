# generatePEM
iOS快速生成推送的pem文件

使用这个文件，我们需要制定一个规范，不然肯定是不成功的，我不是很喜欢制定规则的人，但是由于技术有限，所以必须这样

1.我们最好先创建一个文件夹，为了便于管理证书。该文件夹下应该有生产的cer，p12和生产的cer，p12，总共四个证书。
2.格式需要如下python /Users/huxiang/Desktop/generateCER.py -dev=/Users/huxiang/Desktop/cer-p12/aps_development.cer,/Users/huxiang/Desktop/cer-p12/aps_development.p12 -dis=/Users/huxiang/Desktop/cer-p12/aps_distribution.cer,/Users/huxiang/Desktop/cer-p12/aps_distribution.p12 -val=true
3.注意像这个-dev=文件.p12,文件.cer这两个文件是没有先后顺序的，其次，如果你是先直接拖拽文件进去的时候，默认会在文件后面加空格，需要去掉空格。
4.字段说明:-dev后面是接的开发证书。-dis后面的是生产证书。-val后面意思是否验证证书，传入ture代表验证证书，默认不验证，一般不会出问题的。

