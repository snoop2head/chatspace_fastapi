# Chatspace Fastapi
### Korean spacing API server made with [FastAPI](https://github.com/tiangolo/fastapi) and [Chatspace](https://github.com/pingpong-ai/chatspace)

In previous project, [Chatspace API was built with Flask.](https://github.com/snoop2head/chatspace_api)
Along with it, this project builds Chatspace API server with [the FastAPI.](https://github.com/tiangolo/fastapi)

Chatspace is Korean Sentence spacing module according to grammar. Being developed by chatbot company scatterlab, it shows good performance for proofreading. 

But Chatspace uses torch as dependency. On linux, torch module takes up 750MB of disk space in linux environment. Thus it’s too heavy to run with other applications on the same server. 


### Input Format Sample: url + query
http://127.0.0.1:8000/proofread/아버지가방에들어가신다

### Output Format Sample: json
```json
{
"success": true,
"spaced_text": "아버지가 방에 들어가신다"
}
```
