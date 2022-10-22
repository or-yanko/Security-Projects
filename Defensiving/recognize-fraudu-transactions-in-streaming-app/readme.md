1. install kafka - brew install kafka
2. install java from web
3. activate zookeeper - /usr/local/bin/zookeeper-server-start /usr/local/etc/zookeeper/zoo.cfg
4. in new terminal activate kafka - /usr/local/bin/kafka-server-start /usr/local/etc/kafka/server.properties
5. send frouds with - python producer.py
6. detect it with - python detector.py
7. detect web with - python main-detector-app.py

those are show froud if amount>900 else show legit
