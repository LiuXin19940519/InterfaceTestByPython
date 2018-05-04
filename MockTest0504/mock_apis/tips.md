具体可参考：
https://www.cnblogs.com/weke/articles/6859021.html、
https://blog.csdn.net/crisschan/article/details/53335234

1.若moco-runner-standalone.jar文件和mock的接口（json文件）在同一目录下，
则执行java -jar moco-runner-0.12.0-standalone.jar http -p 12306 -c xxx.json

2.若moco-runner-standalone.jar文件和mock的接口（json文件）不在同一目录下（需要先新建config文件引导指向正确目录），
则执行java -jar moco-runner-0.12.0-standalone.jar http -p 12306 -c Configs.json
