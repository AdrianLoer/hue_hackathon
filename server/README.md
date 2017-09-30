'''
docker build -t hue_server .

'''


'''
docker run -d --name hue_server hue_server
'''


'''
docker rm -f hue_server
'''


'''
docker run -d --name hue_server -e VIRTUAL_HOST=ws.10.1.228.146 --expose 8080 hue_server
'''