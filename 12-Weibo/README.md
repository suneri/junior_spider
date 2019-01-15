## Header
Accept: */*<br>
Accept-Encoding: gzip, deflate, br<br>
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7<br>
Connection: keep-alive<br>
Content-Length: 336<br>
Cache-Control: no-cache<br>
Content-Type: application/x-www-form-urlencoded<br>
Origin: https://passport.weibo.cn<br>
Referer: https://passport.weibo.cn/signin/login<br>
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36<br>

## www-url-encoded body (raw)
username=18600663368&password=B69-FNw-Crq-BmT&savestate=1&r=https%3A%2F%2Fm.weibo.cn%2Fstatus%2FHbclHn7NG%3F&ec=0&pagerefer=https%3A%2F%2Fpassport.weibo.cn%2Fsignin%2Fwelcome%3Fentry%3Dmweibo%26r%3Dhttps%253A%252F%252Fm.weibo.cn%252Fstatus%252FHbclHn7NG%253F&entry=mweibo&wentry=&loginfrom=&client_id=&code=&qq=&mainpageflag=1&hff=&hfp=

## www-url-encoded body (parsed)
username: 18600663368<br>
password: B69-FNw-Crq-BmT<br>
savestate: 1<br>
r: https://m.weibo.cn/status/HbclHn7NG?<br>
ec: 0<br>
pagerefer: https://passport.weibo.cn/signin/welcome?entry=mweibo&r=https%3A%2F%2Fm.weibo.cn%2Fstatus%2FHbclHn7NG%3F<br>
entry: mweibo<br>

## API
### Login Url
https://passport.weibo.cn/sso/login

### Post
https://m.weibo.cn/status/HbclHn7NG?

Response is HTML, Use ***$render_data variable***<br>
>id = 4326690815511532<br>
>mid = 4326690815511532<br>

### Replies
***mid*** and ***max_id_type*** are returned from previous request

>https://m.weibo.cn/comments/hotflow?id=4326690815511532&mid=4326690815511532&max_id_type=0<br>
>https://m.weibo.cn/comments/hotflow?id=4326690815511532&mid=4326690815511532&max_id=151614496548072&max_id_type=0<br>
>https://m.weibo.cn/comments/hotflow?id=4326690815511532&mid=4326690815511532&max_id=151202182752583&max_id_type=0<br>

refer to ***pic_post.html*** and ***video_post.html*** for more details