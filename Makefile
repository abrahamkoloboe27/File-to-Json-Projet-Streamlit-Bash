build : 
	docker build -t streamlit-app-file-to-json .
push : 
	docker tag streamlit-app-file-to-json zach27/file-to-json:latest
	docker push zach27/file-to-json:latest
run :
	docker run -p 8501:8501 streamlit-app-file-to-json
build-run : build run