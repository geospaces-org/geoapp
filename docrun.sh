docker run --rm -it --name stream1 -p 8888:8888 -p 7003:7003  --network demonet geospaces/test:streamdev


echo ** To COMMIT YOUR IMAGE ***
	echo docker commit stream1 streamdev
	echo docker tag streamdev geospaces/test:streamdev 
	echo docker push geospaces/test:streamdev 
