
# -*- coding: cp949 -*-
import mimetypes
import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.base64mime import body_encode as encode_base64

"""
Gmail 연동
ID : kpuscriptproject@gmail.com
PW : jgh7339**!
"""

host = "smtp.gmail.com" # Gmail STMP 서버 주소.
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
    title = "영화 정보 프로그램의 발송 메세지 입니다."  # 메일 제목 고정
    senderAddr = "kpuscriptproject@gmail.com"  # 발신 아이디 고정
    recipientAddr = address  # 수신 아이디 입력 받음
    msgtext = "서울시 영화 정보"  # 안내 메세지 고정
    passwd = "jgh7339**!"  # 발신 아이디 비밀번호 고정

    for i in range(10):
        html += '['+str(i+1)+'] '+movie_ranking[i]['movieNm']+"<br>"
        html += "개봉일: " +movie_ranking[i]['openDt']+"<br>"
        html += "누적 관람객: "+movie_ranking[i]['audiAcc']+"<br>"
        html += "당일 관람객: "+movie_ranking[i]['audiCnt']+"<br><br>"

    # MIMEMultipart의 MIME을 생성합니다.
    from email.mime.multipart import MIMEMultipart

    # Message container를 생성합니다.
    msg = MIMEMultipart('alternative')

    # set message
    msg['Subject'] = title
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
    msg.attach(msgPart)
    msg.attach(bookPart)

    print("connect smtp server ... ")
    s = MySMTP(host, port)
    # s.set_debuglevel(1)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderAddr, passwd)  # 로긴을 합니다.
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

    print("Mail sending complete!!!")




































