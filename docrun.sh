NW=--network demonet
docker network ls | grep demonet ; if [ $? -ne 0 ]; then docker network create demonet ; fi

docker run --rm -it --name stream1 -p 8888:8888 -p 7003:7003  --network demonet geospaces/test:streamdev


echo ** To COMMIT YOUR IMAGE ***
	echo docker commit stream1 streamdev
	echo docker tag streamdev geospaces/test:streamdev 
	echo docker push geospaces/test:streamdev 
docker commit stream1 streamdev; docker tag streamdev geospaces/test:streamdev; docker push geospaces/test:streamdev


#To run it on arm64 arch machines first install following:

docker run --privileged --rm tonistiigi/binfmt --install all
