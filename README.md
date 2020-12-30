# xtunnel_checkin

功能：https://xtunnel-aff.icu/auth/register?code=l95E 自动签到，每日获取50 MB 流量

## Ready

需要 Python 模块

```
requests
ast
PyYaml
alive_progress
colorama
```

配置文件 `config.yaml` 填写

```yaml
---
email : "ybmgaoyu@foxmail.com"

password : "xxxxxxxxxxxxxxxxxxxxxxxxx"
#	选填
cookie : ""
```

## RUN

```shell
➜  xtunnel_checkin python3 main.py


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
您似乎已经签到过了...
```

