__author__ = 'Super.JZ'
class HtmlOutputer():
    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if not data:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open("output.html", 'w+')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"% data['url'])
            fout.write("<td>%s</td>"% data['title'])
            fout.write("<td>%s</td>"% data['summary'].encode('gb18030').decode('gbk','ignore')) #2.encode把数据变成了bytes形式
                                                                                                #4.用gbk不行，因为gbk不包括utf-8里的内容，会报错
                                                                                                #3.用utf-8不行，与后面的gbk不兼容显示乱码
                                                                                                #1.decode必须与平台（cmd）兼容所以必须是gbk才不会报错
                                                                                                #5.猜测python3自动从脚本的编码输出时转换用的是.encode('gbk').decode('gbk', 'ignore')
            fout.write("</tr>")                                                                 #6.encode('gb2312').decode('gbk', 'ignore'),得到UnicodeEncodeError: 'gb2312' codec can't encode character '\u02c8' in position 13: illegal multibyte sequence，证实5
			
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()