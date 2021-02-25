# xtunnel_checkin

## Features

* https://xtunnel-aff.icu/auth/register?code=l95E 自动签到，每日获取50 MB 流量
* 自动每天定时签到

## 使用

### 安装

需要 Python 模块

```
requests
ast
PyYaml
alive_progress
colorama
```

`sudo python3 -m pip install -r requirements.txt`

### 配置

配置文件 `config.yaml` 填写

```yaml
---
email : "ybmgaoyu@foxmail.com"

password : "xxxxxxxxxxxxxxxxxxxxxxxxx"
#	选填
cookie : ""
```

### 运行

```shell
➜  xtunnel_checkin python3 run.py -c config.yaml


               __  ___            __       __      ___     //
        \ / /  / /   //   / / //   ) ) //   ) ) //___) ) //
         \/ /  / /   //   / / //   / / //   / / //       //
         / /\ / /   ((___( ( //   / / //   / / ((____   //



            ___     / __      ___      ___     / ___       ( )   __
          //   ) ) //   ) ) //___) ) //   ) ) //\ \       / / //   ) )
         //       //   / / //       //       //  \ \     / / //   / /
        ((____   //   / / ((____   ((____   //    \ \   / / //   / /



功能：xtunnel 自动打卡，每日获取50 MB 流量
|████████████████████████████████████████| 1/1 [100%] in 1.5s (0.65/s)
登录成功
|████████████████████████████████████████| 1/1 [100%] in 8.2s (0.12/s)
签到成功，您获取了50MB流量
```

## 定时任务

可以通过脚本设置定时任务（默认每天临晨4点自动签到）

`sudo sh task.sh`



此项目仅限于学习研究