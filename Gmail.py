
# -*- coding: cp949 -*-
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.base64mime import body_encode as encode_base64

"""
Gmail ����
ID : kpuscriptproject@gmail.com
PW : jgh7339**!
"""

host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
port = "587"

class MySMTP(smtplib.SMTP):
    def login(self, user, password):
        def encode_cram_md5(challenge, user, password):
            challenge = base64.decodestring(challenge)
            response = user + " " + hmac.HMAC(password, challenge).hexdigest()
            return encode_base64(response)

        def encode_plain(user, password):
            s = "\0%s\0%s" % (user, password)
            return encode_base64(s.encode('ascii'), eol='')

        AUTH_PLAIN = "PLAIN"
        AUTH_CRAM_MD5 = "CRAM-MD5"
        AUTH_LOGIN = "LOGIN"

        self.ehlo_or_helo_if_needed()

        if not self.has_extn("auth"):
            raise SMTPException("SMTP AUTH extension not supported by server.")

        authlist = self.esmtp_features["auth"].split()
        preferred_auths = [AUTH_CRAM_MD5, AUTH_PLAIN, AUTH_LOGIN]

        authmethod = None
        for method in preferred_auths:
            if method in authlist:
                authmethod = method
                break

        if authmethod == AUTH_LOGIN:
            (code, resp) = self.docmd("AUTH",
                                      "%s %s" % (AUTH_LOGIN, encode_base64(user)))
            if code != 334:
                raise SMTPAuthenticationError(code, resp)
            (code, resp) = self.docmd(encode_base64(password))
        elif authmethod == AUTH_PLAIN:
            temp_encode_plain = str(encode_plain(user, password))
            temp_encode_plain = temp_encode_plain.replace("\n", "")
            (code, resp) = self.docmd("AUTH",
                                      AUTH_PLAIN + " " + temp_encode_plain)
        elif authmethod == AUTH_CRAM_MD5:
            (code, resp) = self.docmd("AUTH", AUTH_CRAM_MD5)
            if code == 503:
                return (code, resp)
            (code, resp) = self.docmd(encode_cram_md5(resp, user, password))
        elif authmethod is None:
            raise SMTPException("No suitable authentication method found.")
        if code not in (235, 503):
            raise SMTPAuthenticationError(code, resp)
        return (code, resp)

def SendMail(address, movie_ranking):
    global host, port
    html = ""
    title = "��ȭ ���� ���α׷��� �߼� �޼��� �Դϴ�."  # ���� ���� ����
    senderAddr = "kpuscriptproject@gmail.com"  # �߽� ���̵� ����
    recipientAddr = address  # ���� ���̵� �Է� ����
    msgtext = "����� ��ȭ ����"  # �ȳ� �޼��� ����
    passwd = "jgh7339**!"  # �߽� ���̵� ��й�ȣ ����

    for i in range(10):
        html += '['+str(i+1)+'] '+movie_ranking[i]['movieNm']+"<br>"
        html += "������: " +movie_ranking[i]['openDt']+"<br>"
        html += "���� ������: "+movie_ranking[i]['audiAcc']+"<br>"
        html += "���� ������: "+movie_ranking[i]['audiCnt']+"<br><br>"

    # MIMEMultipart�� MIME�� �����մϴ�.
    from email.mime.multipart import MIMEMultipart

    # Message container�� �����մϴ�.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # �޼����� ������ MIME ������ ÷���մϴ�.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # �α��� �մϴ�.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")




































