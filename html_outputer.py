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
            fout.write("<td>%s</td>"% data['summary'].encode('gb18030').decode('gbk','ignore')) #2.encode�����ݱ����bytes��ʽ
                                                                                                #4.��gbk���У���Ϊgbk������utf-8������ݣ��ᱨ��
                                                                                                #3.��utf-8���У�������gbk��������ʾ����
                                                                                                #1.decode������ƽ̨��cmd���������Ա�����gbk�Ų��ᱨ��
                                                                                                #5.�²�python3�Զ��ӽű��ı������ʱת���õ���.encode('gbk').decode('gbk', 'ignore')
            fout.write("</tr>")                                                                 #6.encode('gb2312').decode('gbk', 'ignore'),�õ�UnicodeEncodeError: 'gb2312' codec can't encode character '\u02c8' in position 13: illegal multibyte sequence��֤ʵ5
			
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()