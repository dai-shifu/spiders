# 使用action 做定时任务
- spider_vpn，抓取我再用的vpn地址，通过微信发送给我，即时更新地址。

登录和推送使用环境变量 `EMAIL`、`PASSWD`、`SEND_KEY`、`SEND_KEY_BB`。可选的 `LOGIN_URL`、`IOS_TUTORIAL_URL`、`WINDOWS_TUTORIAL_URL` 用于覆盖默认网址；GitHub Actions 中可设置同名仓库变量。
