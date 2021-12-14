import yaml
#通过调用方法自动的生产yaml文件
t = open("config.yaml","w")
env = {
    "default": "pro",
    "test": "test-eduzone.codemao.cn",
    "staging": "staging-eduzone.codemao.cn",
    "pro": "eduzone.codemao.cn"
}
yaml.safe_dump(env,t)

