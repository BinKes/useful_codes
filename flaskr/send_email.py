from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart, MIMEBase
from email.mime.image import MIMEImage


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#mail_msg = 'hello, send by Python...'

'''
 邮件header信息，用于帮助邮件程序（服务器程序和客户端程序）正确处理邮件(发送、转发、显示等)，常用的header：
To header： 表明邮件接收人
From header：向用户表明邮件的发件人
Subject header：显示邮箱的摘要信息
Date header：用来按照到达时间分类邮箱
Message-ID header：需要确保产生的Message ID与世界上其他任何邮件都不一样。”@”右边部分是产生这个Message ID的主机全名，这就保证了Message ID是依赖一个唯一的计算机的。而”@”右边的部分是由时间、产生ID的程序进程ID以及一些随机数据联合产生。Message-ID和In-Reply-To header可以帮助邮件服务程序分层次显示邮件。
MIME header：可以帮助邮件程序以合适的语言、格式来显示邮件，它们也用来处理附件。
'''
def send_email(mail_msg, subtype):
    # 输入Email地址和口令:
    from_addr = 'hui.zou@jiukangyun.com'
    password = ''
    # 输入收件人地址:
    to_addr = '289087901@qq.com'

    # 输入SMTP服务器地址:
    smtp_server = 'smtp.exmail.qq.com'
    msg = MIMEText(mail_msg, subtype, 'utf-8')
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    try:
        server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)

def send_email_with_attach():
    # 首先要创建MIMEMultipart()实例
    '''
    from_addr = 'hui.zou@jiukangyun.com'
    password = ''
    # 输入收件人地址:
    to_addr = '289087901@qq.com'

    # 输入SMTP服务器地址:
    smtp_server = 'smtp.exmail.qq.com'
    msg = MIMEMultipart('related')
    msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()
    
    # 指定图片为当前目录
    fp = open('jkom.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgRoot = MIMEMultipart('alternative')
    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    
    mail_msg = """
                <p>Python 邮件发送测试...</p>
                <p><a href="http://www.runoob.com">教程链接</a></p>
                <p>图片演示：</p>
                <p><img src="cid:image1"></p>
                """
    try:
        msgRoot.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    except Exception as e:
        print(e)
    msg.attach(msgImage)
    msg.attach(msgRoot)
    # 开始构造附件
    att_file1 = MIMEText(open('requirements.txt', 'rb').read(), 'base64', 'utf-8')
    att_file1['Content-Type'] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att_file1["Content-Disposition"] = 'attachment; filename = "sdfsfsf.txt"'
    msg.attach(att_file1)

    with open('jkom.png', 'rb') as f:
        mime = MIMEBase('image', 'png', filename='jkom.png')
        mime.add_header('Content-Disposition', 'attachment', filename='jkom.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    try:
        server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件")
        print(e)'''
    
    sender = 'hui.zou@jiukangyun.com'
    password = ''
    receivers = ['289087901@qq.com']
    smtp_server = 'smtp.exmail.qq.com'

    msgRoot = MIMEMultipart('related')
    msgRoot['From'] = Header("菜鸟教程", 'utf-8')
    msgRoot['To'] =  Header("测试", 'utf-8')
    subject = 'Python SMTP 邮件测试'
    msgRoot['Subject'] = Header(subject, 'utf-8')

    #msgAlternative = MIMEMultipart('alternative')
    #msgRoot.attach(msgAlternative)
    mail_msg = """
    <p>Python 邮件发送测试...</p>
    <p><a href="http://www.runoob.com">教程链接</a></p>
    <p>图片演示：</p>
    <p><img src="cid:image1"></p>
    """
    msgRoot.attach(MIMEText(mail_msg, 'html', 'utf-8'))

    # 指定图片为当前目录
    fp = None
    try:
        fp = open('jkom.png', 'rb')
    except Exception as e:
        print(e)
    msgImage = MIMEImage(fp.read())
    fp.close()

    # 定义图片 ID，在 HTML 文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)

    try:
        server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.login(sender, password)
        server.sendmail(sender, receivers, msgRoot.as_string())
        print ("邮件发送成功")
        server.quit()
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")


if __name__ == '__main__':
    mail_msg = '<html><body><h1>Hello</h1>' +\
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +\
    '</body></html>'
    subtype = 'html'
    # subtype = 'plain'
    # mail_msg
    #send_email(mail_msg, subtype)
    send_email_with_attach()