### this file provide class that contain Notice subject, content, link ###

class Script:
    subject = ""
    content = "" # html type #
    link = ""
        
    def make_script(self, posts, link, website):
        
        self.content = '''
        <head>
        <style>
        button{
            border-style: none;
            background-color: rgba(145, 143, 222, 0.648);
            border-radius: 28px;
            
            margin-left: 10%;
        }
        h1, h2{
            color: black;
        }
        a{
            text-decoration: none;
            color: rgba(42, 40, 40, 0.58);
            font-size: large;
        }
        </style>
        </head>
        <body>
        <img src="http://notice-alarm.com/static/image/logo.png" alt="notice-alarm logo">
        <br>
        <h2>''' + website + "</h2>\n"
        
        for post in posts:
            self.content += "<h2>%s</h2>\n" % post

        self.content += '''
        <p style="font-size: larger;">
        ✅ 새로운 공지가 추가되었어요!<br>
        <br>
        ✅ 사용자님이 원하시는 내용이라면, 아래 버튼을 눌러 공지사항을 확인해보세요!<br>
        </p>
        <br>
        <button><a href="''' + link + '''" target="_blank">📢 바로가기 📢</a></button>
        </body>
        '''
        
        
        self.subject = '[' + website + ']' + ' '
        if len(posts) == 1:
            self.subject += posts[0]
        else:
            self.subject += str(len(posts)) + '개의 게시글이 등록되었습니다.'
        
    
    